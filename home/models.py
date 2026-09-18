from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    value = models.CharField(max_length=50, default="OFF")

    def __str__(self):
        return self.name