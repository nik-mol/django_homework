# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import redirect
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListCreateAPIView, RetrieveAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     UpdateAPIView)

from .models import Measurement, Sensor
from .serializers import MeasurementSerializer, SensorDetailSerializer


def home(request):
    return redirect('list-create-sensors')

class ListCreateSensors(ListCreateAPIView):
    queryset = Sensor.objects.all()    
    serializer_class = SensorDetailSerializer

class CreateMeasurement(CreateAPIView):
    queryset = Measurement.objects.all()    
    serializer_class = MeasurementSerializer

class UpdateSensor(UpdateAPIView):
    queryset = Sensor.objects.all()    
    serializer_class = SensorDetailSerializer

class OneSensor(RetrieveAPIView):
    queryset = Sensor.objects.all()    
    serializer_class = SensorDetailSerializer

class DeleteSensor(DestroyAPIView):
    queryset = Sensor.objects.all()    
    serializer_class = SensorDetailSerializer

class DetalSensor(RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()    
    serializer_class = SensorDetailSerializer

class DeleteMeasurement(DestroyAPIView):
    queryset = Measurement.objects.all()    
    serializer_class = MeasurementSerializer
