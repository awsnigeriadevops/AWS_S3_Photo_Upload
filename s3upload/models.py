from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage


class S3File(models.Model):
    # Define a field for the file
    file = models.FileField(upload_to="s3files/")

    # You can include additional fields as needed
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.file.name
