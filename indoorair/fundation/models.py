from django.db import models
from django.contrib.auth.models import User

class Instrument(models.Model):
    user = models.ForeignKey(
      User,
      on_delete = models.CASCADE
    )
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name + " " + str(self.user)


class Sensor(models.Model):
    instrument = models.ForeignKey(
      to ='instrument',
      on_delete = models.CASCADE
    )
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name + " " + str(self.instrument)

class TimeSeriesDatum(models.Model):
    sensor = models.ForeignKey(
      to ='Sensor',
      on_delete = models.CASCADE
    )
    value = models.FloatField()
    time =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.value) + " at" + str(self.sensor)
