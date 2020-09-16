from rest_framework import mixins
from rest_framework.generics import GenericAPIView, RetrieveAPIView, CreateAPIView

from .serializers import TraslationSerializer, TraslationResultSerializer, Traslation


class TraslationCreateAPIView(CreateAPIView):
    serializer_class = TraslationSerializer


class TraslationRetreiveAPIView(RetrieveAPIView):
    lookup_field = "id"
    queryset = Traslation.objects.all()
    serializer_class = TraslationResultSerializer
