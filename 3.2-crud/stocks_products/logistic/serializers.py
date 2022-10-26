from email.policy import default
from rest_framework import serializers

from .models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    # настройте сериализатор для продукта
    class Meta:
        model = Product
        fields = '__all__'


class ProductPositionSerializer(serializers.ModelSerializer):
    # сериализатор для позиции продукта на складе
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']  


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    # сериализатор для склада
    class Meta:
        model = Stock
        fields = ['address', 'positions']

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
             
        # создаем склад по его параметрам
        stock = super().create(validated_data)
        # stock = Stock.objects.create(**validated_data)  # ---2-ой способ создания склада----

        #Заполнение связанной таблицы StockProduct с помощью списка positions     
        for position in positions: 
            StockProduct.objects.create(
                stock = stock,
                **position
                # product = position.get('product'),
                # quantity = position.get('quantity'),   #--- 2-ой вариант заполнения вместо **position-------
                # price = position.get('price')
            )

        # [StockProduct.objects.bulk_create([
        #     StockProduct(
        #     stock = stock,
        #     product = position.get('product'),
        #     quantity = position.get('quantity'),  # ----2-ой способ с помощью "bulk_create" 
        #     price = position.get('price')
        #     )
        # ]) for position in positions]
        
        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')      
      
        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)
        # ---2-ой способ--------
        # instance.address = validated_data.get('product', instance.address)
        # instance.save() 
      
        # обновляем связанную таблицу StockProduct       
        for position in positions: 
            default = {                
                'product' : position.get('product'),
                'quantity' : position.get('quantity'),
                'price' : position.get('price'),
            }
            StockProduct.objects.update_or_create(
                stock = stock,                
                product = position.get('product'), 
                quantity = position.get('quantity'),
                price = position.get('price'),
                defaults = default            
            )    
                
        return stock
