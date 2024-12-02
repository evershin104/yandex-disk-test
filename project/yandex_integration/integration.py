from typing import Dict

import requests
import json

from django.http import JsonResponse

from project import settings


class YandexDiskIntegration:

    def __init__(self, public_key: str) -> None:
        self.api = settings.YANDEX_CLOUD
        self.public_key = public_key


    @staticmethod
    def extract_items_preview_links(response: Dict) -> Dict:
        items = response.get('_embedded', dict()).get('items', [])
        previews = []

        for item in items:
            preview = item.get('preview')
            if preview:
                previews.append({
                    'name': item.get('name'),
                    'preview': preview,
                    'download': item.get('file')
                })
        return {'previews': previews}


    def get_resource_preview(self):
        try:
            response = requests.get(self.api, params={"public_key": self.public_key})
            if response.ok:
                dict_response = response.json() or {}
                return self.extract_items_preview_links(dict_response)
            else:
                JsonResponse({'error': 'Ошибка подключения к Я.Диск'}, status=response.status_code)
        except requests.RequestException as e:
            return JsonResponse({'error': 'Ошибка подключения к Я.Диск'}, status=500)
