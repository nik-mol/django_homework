from django.urls import path

from .views import (CreateMeasurement, DeleteMeasurement, DeleteSensor,
                    DetalSensor, ListCreateSensors, OneSensor, UpdateSensor)

urlpatterns = [    
    path('sensors/', ListCreateSensors.as_view(), name='list-create-sensors'),   
    path('measurements/', CreateMeasurement.as_view(), name='create-measurements'),
    path('sensor/<int:pk>', UpdateSensor.as_view(), name='update-sensors'),
    path('sensorview/<int:pk>', OneSensor.as_view(), name='view-sensor'),
    path('deletesensor/<int:pk>', DeleteSensor.as_view(), name='delete-sensor'),
    path('detalsensor/<int:pk>', DetalSensor.as_view(), name='detal-sensor'),
    path('delete/<int:pk>', DeleteMeasurement.as_view()),
]
