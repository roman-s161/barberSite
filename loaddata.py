from django.core.management import call_command
import json

# Загружаем весь дамп файл
with open('dump.json', 'r') as f:
    data = json.load(f)

# Определяем порядок загрузки моделей с учетом зависимостей
# Каждый ключ - это модель, значение - список моделей, от которых она зависит
model_order = {
    'auth.permission': [],          # Разрешения - базовая модель
    'auth.user': [],               # Пользователи
    'contenttypes.contenttype': [], # Типы контента
    'core.service': [],            # Услуги - независимая модель
    'core.master': ['core.service'],     # Мастера зависят от услуг
    'core.visit': ['core.master', 'core.service'],  # Визиты зависят от мастеров и услуг
    'core.review': ['core.master']       # Отзывы зависят от мастеров
}

# Создаем отдельные файлы фикстур для каждой модели и загружаем их
for model_name in model_order:
    # Фильтруем данные для текущей модели
    model_data = [item for item in data if item['model'] == model_name]
    if model_data:
        # Сохраняем во временный файл
        with open(f'{model_name}.json', 'w') as f:
            json.dump(model_data, f)
        try:
            # Пытаемся загрузить данные
            call_command('loaddata', f'{model_name}.json')
            print(f"Успешно загружены данные для {model_name}")
        except Exception as e:
            print(f"Ошибка при загрузке {model_name}: {e}")
