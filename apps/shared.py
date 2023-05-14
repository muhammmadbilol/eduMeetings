import os

from django.db import models
from django.utils.text import slugify


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SlugModel(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super().save(*args, **kwargs)

    class Meta:
        abstract = True


def rename_image(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return f'{instance._meta.app_label}s/images/{instance.slug}{filename_ext}'
