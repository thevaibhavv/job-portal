from rest_framework import serializers #type:ignore
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    posted_by = serializers.ReadOnlyField(source='posted_by.username')

    class Meta:
        model = Job
        fields = 'all'
        read_only_fields = ["posted_by", "created_at"]