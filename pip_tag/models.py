from django.db import models

# Create your models here.
class Data(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField('time',auto_now=True)
    temp = models.DecimalField('temp', max_digits=8, decimal_places=2)
    light = models.IntegerField('light')
    humidity = models.IntegerField('humidity')

    def __str__(self):
        return "temperature:{};light:{};humidity:{}".format(self.temp, self.light, self.humidity)