from rest_framework import serializers
from .models import Drink, Completedtasks
class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'task', 'dueDate', 'urgency']
class CompletedtasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Completedtasks
        fields = ['id', 'task', 'urgency']