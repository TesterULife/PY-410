from django.db import models
from django.utils import timezone


class Files(models.Model):
    file_name = models.CharField(max_length=250)
    file_type = models.CharField(max_length=64)
    file_path = models.TextField('file_path')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'


class Logs(models.Model):
    class Status(models.TextChoices):
        UPLOAD = 'upload', 'Upload'
        GET = 'get', 'Get'
        DELETE = 'delete', 'Delete'

    file = models.ForeignKey(
        Files,
        on_delete=models.CASCADE,
        related_name='logs'
    )

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.UPLOAD
    )

    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Log'
        verbose_name_plural = 'Logs'