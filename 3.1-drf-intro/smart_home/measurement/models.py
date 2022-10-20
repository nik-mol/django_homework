from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Сенсор'
        verbose_name_plural = 'Сенсоры'
        ordering = ['name']

class Measurement(models.Model):
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, upload_to='photos')


    class Meta:
        verbose_name = 'Температура'
        verbose_name_plural = 'Температуры'
        ordering = ['created_at']


