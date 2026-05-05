from django.db import models
from django.utils import timezone


class Files(models.Model):
    file_name = models.CharField(max_length=250)
    file_type = models.CharField(max_length=64)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    @property
    def clean_name(self):
        parts = self.file_name.split('_', 1)

        if len(parts) > 1:
            return parts[1]

        return self.file_name

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'
