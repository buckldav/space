from django.db import models


# Create your models here.
class FlightControl(models.Model):
    is_online = models.BooleanField(default=True)
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name
