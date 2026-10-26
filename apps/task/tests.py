from django.test import TestCase
from django.core.cache import cache
from rest_framework.test import APIClient
from rest_framework import status

from .models import Task


class SimpleTaskCachingTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        cache.clear()
        self.task = Task.objects.create(
            title="Купить хлеб",
            description="Свежий батон"
        )

    def test_caching_flow(self):
        # 1. Первый запрос: кэш пустой, данные читаются из базы
        res1 = self.client.get("/task/")
        self.assertEqual(res1.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res1.data), 1)

        # 2. Проверяем, что в кэше появились данные
        self.assertIsNotNone(cache.get("tasks"))

        # 3. Добавляем новую запись напрямую в базу
        Task.objects.create(title="Купить молоко", description="1 литр")

        # 4. Запрос через API по-прежнему возвращает 1 запись (из кэша)
        res2 = self.client.get("/task/")
        self.assertEqual(len(res2.data), 1)

        # 5. Делаем POST через API — кэш должен очиститься
        post_res = self.client.post("/task/", {"title": "Купить масло", "description": "Пачка"}, format="json")
        self.assertEqual(post_res.status_code, status.HTTP_201_CREATED)
        self.assertIsNone(cache.get("tasks"))

        # 6. Следующий GET вернет уже все 3 актуальные записи
        res3 = self.client.get("/task/")
        self.assertEqual(len(res3.data), 3)
