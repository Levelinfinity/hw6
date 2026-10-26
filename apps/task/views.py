from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from collections import defaultdict

from .models import Task
from .serializers import TaskSerializer


class TaskView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        group_by = request.query_params.get("group_by")
        if group_by == "date":
            grouped_cache_key = "tasks_grouped"
            cached_grouped = cache.get(grouped_cache_key)
            if cached_grouped is not None:
                return Response(cached_grouped)

            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks, many=True)

            grouped_data = defaultdict(list)
            for task_data in serializer.data:
                deadline = task_data.get("deadline")
                if deadline:
                    date_str = deadline.split("T")[0]
                    grouped_data[date_str].append(task_data)
                else:
                    grouped_data["No deadline"].append(task_data)

            result = dict(grouped_data)
            cache.set(grouped_cache_key, result, 60)
            return Response(result)

        tasks_data = cache.get("tasks")
        if tasks_data is not None:
            return Response(tasks_data)

        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        tasks_data = serializer.data

        cache.set("tasks", tasks_data, 60)
        return Response(tasks_data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        cache.delete("tasks")
        cache.delete("tasks_grouped")

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TaskDetailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        cache.delete("tasks")
        cache.delete("tasks_grouped")
        return Response(serializer.data)

    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()

        cache.delete("tasks")
        cache.delete("tasks_grouped")
        return Response({"message": "Задача удалена"}, status=status.HTTP_204_NO_CONTENT)