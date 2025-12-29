from django.contrib.auth.models import AnonymousUser
from job.models import Job
from job.serializers import JobSerializer

class JobService:
    """
    Service layer for Job-related operations.
    Keeps business logic out of views.
    """

    @staticmethod
    def get_all_jobs():
        jobs = Job.objects.all().order_by('-created_at')
        return JobSerializer(jobs, many=True).data

    @staticmethod
    def get_job_by_id(pk):
        try:
            job = Job.objects.get(pk=pk)
            return JobSerializer(job).data
        except Job.DoesNotExist:
            return None

    @staticmethod
    def create_job(data, user=None):
        serializer = JobSerializer(data=data)
        if serializer.is_valid():
            if user and not isinstance(user, AnonymousUser):
                serializer.save(posted_by=user)
            else:
                serializer.save(posted_by=None)
            return serializer.data, None

        return None, serializer.errors

    @staticmethod
    def update_job(pk, data):
        try:
            job = Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            return None, {"error": "Job not found"}

        serializer = JobSerializer(job, data=data)
        if serializer.is_valid():
            serializer.save()  # do NOT overwrite posted_by
            return serializer.data, None

        return None, serializer.errors

    @staticmethod
    def delete_job(pk):
        try:
            Job.objects.get(pk=pk).delete()
            return True
        except Job.DoesNotExist:
            return False
