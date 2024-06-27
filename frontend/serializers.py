from rest_framework import serializers
from .models import TaskSheet

class TaskSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskSheet
        fields = '__all__'