from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from project.yandex_integration.forms import URLForm


class URLSubmitView(View):
    """"""
    def get(self, request, *args, **kwargs):
        """

        Args:
            request:

        Returns:

        """
        return render(request, 'main_page.html', {'url': ''})

    def post(self, request, *args, **kwargs):
        """

        Args:
            request:

        Returns:

        """
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            return JsonResponse({'message': 'URL received successfully!', 'url': url})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
