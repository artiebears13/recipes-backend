from django.db import migrations

def convert_steps(apps, schema_editor):
    Recipe = apps.get_model('recipes', 'Recipe')
    for recipe in Recipe.objects.all():
        steps = recipe.steps
        # Если steps существует, является списком и первый элемент – строка,
        # считаем, что данные ещё не преобразованы
        if steps and isinstance(steps, list) and steps and isinstance(steps[0], str):
            new_steps = [{'description': step} for step in steps]
            recipe.steps = new_steps
            recipe.save(update_fields=['steps'])

def reverse_convert_steps(apps, schema_editor):
    # Если понадобится откат миграции, можно вернуть в виде списка строк.
    Recipe = apps.get_model('recipes', 'Recipe')
    for recipe in Recipe.objects.all():
        steps = recipe.steps
        # Если steps существует и первый элемент – словарь, преобразуем обратно в строки.
        if steps and isinstance(steps, list) and steps and isinstance(steps[0], dict):
            new_steps = [step.get('description', '') for step in steps]
            recipe.steps = new_steps
            recipe.save(update_fields=['steps'])

class Migration(migrations.Migration):

    dependencies = [
        # Укажите зависимость от предыдущей миграции, например:
        ('recipes', '0002_alter_recipe_cooking_time_alter_recipe_steps'),
    ]

    operations = [
        migrations.RunPython(convert_steps, reverse_code=reverse_convert_steps),
    ]
