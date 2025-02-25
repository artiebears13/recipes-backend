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
    # Храним ингредиенты и шаги как JSON-массивы
    ingredients = models.JSONField(help_text="Список ингредиентов в формате JSON")
    steps = models.JSONField(help_text="Список шагов приготовления")
    cooking_time = models.IntegerField(help_text="Время готовки в минутах")
    # Вместо default=list используем null=True и blank=True, чтобы SQLite не пытался установить литерал []
    categories = models.JSONField(blank=True, null=True, help_text="Список категорий")
    time_type = models.CharField(max_length=10, choices=TIME_TYPE_CHOICES, blank=True, null=True)
    picture = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
