from rest_framework import serializers
from .models import Task
from django.utils import timezone

class TaskSerializer(serializers.ModelSerializer):
    time_left = serializers.SerializerMethodField()
    
    class Meta:
        model = Task
        fields = ("id", "title", "description")
        read_only_fields = ("id",)

    def get_time_left(self, obj):
        if not obj.deadline:
            return "Дедлайн не указан"
        
        now = timezone.now()
        diff = obj.deadline - now

        if diff.total_seconds() < 0:
            return "Дедлайн просрочен"
        
        days = diff.days
        if days > 0:
            return f"{days} days left"
        
        hours = int(diff.seconds // 3600)
        return f"{hours} hours left"

    # Валидация поля title
    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Минимум 3 символа в названии!")
        return value.strip()
