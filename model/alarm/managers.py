from django.db import models


class AlarmManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(status=-1)
