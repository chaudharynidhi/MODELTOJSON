from rest_framework import serializers
from .models import Users, ActivityPeriod

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

class ActPeriodSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ActivityPeriod
        fields = '__all__'