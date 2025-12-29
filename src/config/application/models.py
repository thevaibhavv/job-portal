from django.db import models
from django.conf import settings


class Application(models.Model):
    # job = models.ForeignKey(
    #     Job, 
    #     on_delete=models.CASCADE, 
    #     related_name='applications'
    # )

    # Applicant (User)
    applicant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    # Resume / Cover Letter
    resume_text = models.TextField(
        help_text="Paste resume or cover letter here"
    )

    # Application status
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-applied_at']
        unique_together = ('job_id', 'applicant')

    def __str__(self):
        return f"{self.applicant} applied for Job ID {self.job_id}"
