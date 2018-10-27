from rest_framework import serializers

from core.models import Link


class LinkSerializer(serializers.ModelSerializer):
    # Serializer for creating and updating
    def create(self, validated_data):
        attachments = validated_data.pop('assign_files')

        instance = super(LinkSerializer, self).create(validated_data)
        user = self.context.get("request").user
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance = super(LinkSerializer, self).update(instance, validated_data)
        return instance

    class Meta:
        model = Link
        fields = ('id', 'url', 'email')
