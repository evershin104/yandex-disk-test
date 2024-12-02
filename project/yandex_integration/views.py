from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

class URLSubmitView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'main_page.html')

    def post(self, request, *args, **kwargs):
        url = request.POST.get('url')
        if url:
            # Логика обработки URL
            return JsonResponse({'message': 'ok', 'url': url})
        return JsonResponse({'error': 'not ok'}, status=400)
