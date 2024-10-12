Установка и запуск
1. Клонирование репозитория
Клонируйте репозиторий и перейдите в папку проекта:
git clone https://github.com/Bauren/car-management.git
cd car-management

2. Настройка виртуального окружения
Создайте виртуальное окружение и активируйте его:
python -m venv .venv
source .venv/bin/activate  # для Windows: .venv\Scripts\activate

3. Установка зависимостей
Установите зависимости:
pip install -r requirements.txt

4. Применение миграций
Выполните миграции базы данных:
python manage.py migrate

5. Создание суперпользователя
Создайте суперпользователя для доступа к административной панели:
python manage.py createsuperuser

6. Запуск сервера разработки
python manage.py runserver

Использование API
1. Получение списка автомобилей
GET /api/cars/

2. Получение информации о конкретном автомобиле
GET /api/cars/<id>/

3. Создание нового автомобиля
POST /api/cars/ 
Пример тела запроса:

{
  "make": "Toyota",
  "model": "Camry",
  "year": 2021,
  "description": "Компактный седан"
}
4. Обновление информации о конкретном автомобиле
PUT /api/cars/<id>/

5. Удаление автомобиля
DELETE /api/cars/<id>/