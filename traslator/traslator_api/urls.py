from django.urls import path

from .api import TraslationCreateAPIView, TraslationRetreiveAPIView

app_name = 'devices'

urlpatterns = [
    path('translations/', TraslationCreateAPIView.as_view(), name='api-traslations'),
    path('translations/<uuid:id>/', TraslationRetreiveAPIView.as_view(), name='api-traslations-detail'),
]
