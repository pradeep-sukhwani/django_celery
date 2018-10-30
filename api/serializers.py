from rest_framework import serializers

from core.models import Link


class UserEmailSerializer(serializers.ModelSerializer):
    # Serializer for creating and updating
    def create(self, validated_data):
        instance = super(UserEmailSerializer, self).create(validated_data)
        instance.link_email(email=validated_data.get("email"), url=validated_data.getlist("url"))
        return instance

    def update(self, instance, validated_data):
        instance.link_email(email=validated_data.get("email"), url=validated_data.getlist("url"))
        return instance

    class Meta:
        model = Link
        fields = ('id', 'url', 'email')
