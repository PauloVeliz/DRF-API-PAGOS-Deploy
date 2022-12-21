from services.models import Service
from rest_framework import serializers
from expired_payments.models import ExpiredPayment
from users.models import User

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'

class ExpiredPaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExpiredPayment
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name"]
        read_only=("password",)