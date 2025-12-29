from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    # We make applicant read-only so it's not required in the POST body
    applicant = serializers.ReadOnlyField(source='applicant.username')

    class Meta:
        model = Application
        fields = ['id', 'job', 'applicant', 'resume_text', 'status', 'applied_at']
        read_only_fields = ['status', 'applied_at']

    def validate(self, data):
        # Optional: Add logic to check if a user is trying to apply for their own job
        request = self.context.get('request')
        if data['job'].posted_by == request.user:
            raise serializers.ValidationError("You cannot apply for a job you posted.")
        return data