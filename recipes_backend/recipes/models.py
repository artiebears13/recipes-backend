# recipes/models.py
import uuid
from django.db import models

class Recipe(models.Model):
    LEVEL_CHOICES = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )
    TIME_TYPE_CHOICES = (
        ('fast', 'Fast'),
        ('slow', 'Slow'),
    )
    CATEGORY_CHOICES = (
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    description = models.TextField(blank=True, null=True)
    # Храним ингредиенты как JSON-массив (без изменений)
    ingredients = models.JSONField(help_text="Список ингредиентов в формате JSON")
    # Обновлённое поле steps: теперь это массив объектов с полем 'description' и (опционально) 'time'
    steps = models.JSONField(
        help_text="Список шагов приготовления. Каждый шаг должен быть объектом с обязательным ключом 'description' и опциональным числовым ключом 'time' (в минутах)."
    )
    cooking_time = models.IntegerField(help_text="Общее время готовки в минутах")
    # Поле для категорий оставляем как JSONField, позволяющее хранить список (null/blank для SQLite)
    categories = models.JSONField(blank=True, null=True, help_text="Список категорий")
    time_type = models.CharField(max_length=10, choices=TIME_TYPE_CHOICES, blank=True, null=True)
    picture = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
