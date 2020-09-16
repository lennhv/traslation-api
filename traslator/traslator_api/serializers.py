from rest_framework import serializers

from .models import Traslation


class ListField(serializers.ListField):

    def to_representation(self, data):
        _data = data.split(Traslation.SPLIT_CHAR)
        return [self.child.to_representation(item) if item is not None else None for item in _data]


class TraslationSerializer(serializers.ModelSerializer):
    text = ListField(child=serializers.CharField())

    class Meta:
        model = Traslation
        fields = ('id', 'lang_source', 'lang_target', 'text')
        read_only_fields = ('id', 'text')

    def create(self, validated_data):
        return self.Meta.model.\
            objects.create_task(**validated_data)


class TraslationResultSerializer(serializers.ModelSerializer):
    traslation = ListField(child=serializers.CharField())

    class Meta:
        model = Traslation
        fields = ('traslation',)
