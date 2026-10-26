from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here. APIView

class HelloApiView(APIView):
    def get(self, request):
        return Response({
            "message": "я Джанго Рест Фреймворк"
        })

class Profile(APIView):
    def get(self, request):
        return Response({
            "name": "Alisher",
            "age": "19",
            "group": "39-1B"
        })


class ProjectInfoApiView(APIView):
    """
    Эндпоинт с описанием структуры, модулей и логики проекта
    """
    def get(self, request):
        return Response({
            "project": "Geeks Backend REST API",
            "version": "1.0.0",
            "description": "Модульная платформа с каталогом магазинов, библиотекой и трекером задач",
            "architecture": {
                "pattern": "Modular Monolith (Django REST Framework)",
                "database": "SQLite (dev) / PostgreSQL (prod ready)",
                "authentication": "Session & Token-based"
            },
            "apps": {
                "users": {
                    "purpose": "Управление учетными записями пользователей",
                    "features": ["Регистрация", "Вход (логин)", "Выход (логаут)", "Редактирование профиля"]
                },
                "shop": {
                    "purpose": "Торговая площадка (магазины, категории и товары)",
                    "features": ["Каталог магазинов", "Категории товаров", "Товары с ценами и фото", "Фильтрация, поиск и сортировка"]
                },
                "task": {
                    "purpose": "Менеджер задач с оптимизацией и дедлайнами",
                    "features": ["CRUD задач", "Дедлайн и статус выполнения", "Группировка по датам", "Кэширование LocMemCache"]
                },
                "books": {
                    "purpose": "Каталог книг и учет библиотек",
                    "features": ["Библиотеки с адресами", "Книги с привязкой к библиотеке (ForeignKey)"]
                },
                "api": {
                    "purpose": "Служебный модуль и мета-информация",
                    "features": ["Информация о системе", "Визитка разработчика"]
                }
            }
        })