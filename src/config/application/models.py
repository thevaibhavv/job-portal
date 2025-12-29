from django.db import models
from django.db import models
from django.conf import settings
from job.models import Job

class Application(models.Model):
    # The job being applied for
    job = models.ForeignKey(
        Job, 
        on_delete=models.CASCADE, 
        null=True,
        related_name='applications'
    )
    
    # The user (candidate) applying
    applicant = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='my_applications'
    )
    
    # Additional application data
    resume_text = models.TextField(help_text="Paste your resume or cover letter here")
    applied_at = models.DateTimeField(auto_now_add=True)
    
    # Status tracking (Optional but helpful)
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    class Meta:
        # Crucial: Ensures a user can only apply to a specific job once
        unique_together = ('job', 'applicant')
        ordering = ['-applied_at']

    def __str__(self):
        return f"{self.applicant.username} applied for {self.job.title}"

# Create your models here.
