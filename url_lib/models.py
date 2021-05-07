from django.db import models
from django.conf import settings


class Url(models.Model):
    short_url = models.CharField(max_length=50, unique=True)
    full_url = models.TextField(null=False, blank=False)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    used = models.IntegerField(default=0)

    def __str__(self):
        return '{} created: {} --> {}'.format(self.creator, self.full_url, self.short_url)