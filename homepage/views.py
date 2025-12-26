from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

from .models import *


def home_view(request):
    # 1. Mock-данные (имитация базы данных)
    # Представим, что это результат сложного SQL-запроса
    mock_tours = [
        {
            "id": 1,
            "title": "Гастро-тур: Вкус Тосканы",
            "price": "145 000",
            "currency": "RUB",
            "description": "Недельное погружение в винную культуру Италии.",
            # Данные для графика (распределение бюджета)
            "chart_data": {
                "labels": ["Отели", "Транспорт", "Гиды", "Еда", "Маржа"],
                "values": [40, 15, 20, 15, 10],  # Проценты или суммы
                "colors": ["#001F3F", "#3A506B", "#FE0678", "#FFB1C1", "#4BC0C0"]
            }
        },
        {
            "id": 2,
            "title": "Экспедиция: Алтайский Край",
            "price": "85 000",
            "currency": "RUB",
            "description": "Джип-тур по самым диким местам Чуйского тракта.",
            "chart_data": {
                "labels": ["Транспорт", "Проживание", "Экипировка", "Питание", "Маржа"],
                "values": [50, 15, 10, 15, 10],  # Здесь транспорт дороже
                "colors": ["#001F3F", "#3A506B", "#FE0678", "#FFB1C1", "#4BC0C0"]
            }
        },
        {
            "id": 3,
            "title": "Релакс: Мальдивы (All Inc)",
            "price": "320 000",
            "currency": "RUB",
            "description": "Полный пакет для тех, кто устал от аналитики.",
            "chart_data": {
                "labels": ["Отели", "Перелет", "Страховка", "Агентские", "Маржа"],
                "values": [60, 25, 2, 3, 10],
                "colors": ["#001F3F", "#3A506B", "#FE0678", "#FFB1C1", "#4BC0C0"]
            }
        }
    ]

    # 2. Сериализуем данные в JSON строку для передачи в JavaScript
    tours_json = json.dumps(mock_tours)

    context = {
        'tours': mock_tours,  # Для отрисовки карточек (HTML)
        'tours_json': tours_json,  # Для отрисовки графиков (JS)
    }

    return render(request, 'homepage/home_test.html', context)