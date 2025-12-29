from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Application
from .serializers import ApplicationSerializer

class ApplyJobView(APIView):
    # User must be logged in to apply
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = ApplicationSerializer(data=request.data, context={'request': request})
        
        if serializer.is_valid():
            # Save the application and explicitly set the applicant
            serializer.save(applicant=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyApplicationsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Returns only the applications made by the logged-in user
        applications = Application.objects.filter(applicant=request.user)
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)

# Create your views here.
