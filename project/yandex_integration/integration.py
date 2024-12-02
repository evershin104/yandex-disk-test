from typing import Dict, List, Union
import requests
from django.http import JsonResponse
from requests import Response

from project import settings


class YandexDiskIntegration:
    """Class for YDisk integration."""

    def __init__(self, public_key: str) -> None:
        self.api: str = settings.YANDEX_CLOUD
        self.public_key: str = public_key


    @staticmethod
    def extract_items_preview_links(response: Dict) -> Dict[str, List]:
        """Extracts usefull info from YDisk `items`
        Args:
            response: Dict object
        Returns:
            Structured data for each element
        """
        items: List = response.get('_embedded', dict()).get('items', [])
        previews: List = []

        for item in items:
            preview: List[Dict] = item.get('preview')
            previews.append({
                'name': item.get('name'),
                'preview': preview,
                'download': item.get('file')
            })
        return {'previews': previews}


    def get_resource_preview(self) -> Union[Dict, JsonResponse]:
        """Returns structured elements from YDisk
        Returns:
            Structured data for each element OR JsonResponse
                with error
        """
        try:
            response: Response = requests.get(self.api, params={"public_key": self.public_key})
            if response.ok:
                dict_response = response.json() or {}
                return self.extract_items_preview_links(dict_response)
            else:
                JsonResponse({'error': 'Ошибка подключения к Я.Диск'}, status=response.status_code)
        except requests.RequestException as e:
            return JsonResponse({'error': 'Ошибка подключения к Я.Диск'}, status=500)
