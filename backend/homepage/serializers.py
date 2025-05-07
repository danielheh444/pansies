from rest_framework import serializers

from homepage.models import Preview


class PreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preview
        fields = "__all__"
