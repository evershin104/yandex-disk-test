from multiprocessing.managers import public_methods

import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from project.yandex_integration.forms import URLForm
from project.yandex_integration.integration import YandexDiskIntegration


class URLSubmitView(View):
    """"""
    def get(self, request, *args, **kwargs):
        return render(request, 'main_page.html', {'url': ''})

    def post(self, request, *args, **kwargs):
        """

        Args:
            request:
            *args:
            **kwargs:

        Returns:

        """
        form = URLForm(request.POST)
        if form.is_valid():

            integration = YandexDiskIntegration(public_key=form.cleaned_data['url'])
            data = integration.get_resource_preview()
            return JsonResponse({'data': data})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
