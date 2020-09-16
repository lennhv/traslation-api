from django.urls import path

from .api import TraslationCreateAPIView, TraslationRetreiveAPIView

app_name = 'devices'

urlpatterns = [
    path('traslations/', TraslationCreateAPIView.as_view(), name='api-traslations'),
    path('traslations/<uuid:id>/', TraslationRetreiveAPIView.as_view(), name='api-traslations-detail'),
]
