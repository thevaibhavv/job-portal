from django.db import models
from django.conf import settings

class Job(models.Model):
    title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.PositiveIntegerField(null=True, blank=True)
    posted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='jobs',
        null=True,
        blank=True
)

    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.title} - {self.company_name}"