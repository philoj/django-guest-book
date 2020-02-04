from django.db import models


class Entry(models.Model):
    class Meta:
        verbose_name_plural = 'Entries'

    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
