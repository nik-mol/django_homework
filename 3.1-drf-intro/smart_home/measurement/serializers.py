from rest_framework import serializers

from .models import Measurement, Sensor

# TODO: опишите необходимые сериализаторы

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement  # наеменование модели
        fields = ['sensor','temperature', 'created_at', 'image'] # список свойств для отображения ('__all__' - отображение всех полей)


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True) 
    # 'many' - данных придет несколько; 
    # 'read_only' - чтобы поле использовалось только для чтения, 
    # но не использовалось при создании или обновлении экземпляра во время десериализации

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


