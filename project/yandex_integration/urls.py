from django.urls import path
from . import views
from .views import URLSubmitView

urlpatterns = [
    path('main-page/', URLSubmitView.as_view(), name='main_page'),
]