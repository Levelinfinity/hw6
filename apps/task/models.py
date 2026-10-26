from django.db import models
from django.utils import timezone 

class Task(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField(null=True, blank=True, verbose_name='Дедлайн')
    is_completed = models.BooleanField(default=False, verbose_name='Выполнено')

    def __str__(self):
        return self.title
