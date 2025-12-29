from django.urls import path
from .views import ApplyJobView, MyApplicationsView

urlpatterns = [
    # POST to /api/apply/ to submit an application
    path('submit/', ApplyJobView.as_view(), name='apply_job'),
    
    # GET to /api/apply/my-apps/ to see your history
    path('my-apps/', MyApplicationsView.as_view(), name='my_applications'),
]