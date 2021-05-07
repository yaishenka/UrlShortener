from rest_framework import serializers
from .models import Url


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ('short_url', 'full_url', 'creator', 'date_created', 'used')
        read_only_fields = ('creator', 'date_created', 'used')
