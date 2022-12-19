from rest_framework import serializers
from .models import Pago,Usuario

class PagoSerializer(serializers.ModelSerializer):
    usuario = serializers.SlugRelatedField(queryset = Usuario.objects.all(),slug_field='email')
    class Meta:
        model = Pago
        fields = '__all__'
    
    def validate_servicio_v1(self,value):
        if value.lower() not in ['netflix','amazon video','star+','paramount+']:
            raise serializers.ValidationError('Error, las opciones de servicio son [Netflix,Amazon Video,Star+,Paramount+]')
        return value
