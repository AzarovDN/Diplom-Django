#Установка проекта

1. Скачать проект с гит
2. Создать виртуальное окружение `python3 -m venv myvenv`
3. Запустить виртуальное окружение `source myvenv/bin/activate`
4. Установить зависимости `pip install -r requirements.txt`
5. В настройках проекта diplom/diplom/settings.py указать свою временную зону. Взять можно [здесь][https://en.wikipedia.org/wiki/List_of_tz_database_time_zones][]
6. В настройках проекта diplom/diplom/settings.py указать свой SECRET_KEY
7. Генерируем миграции `python manage.py makemigrations`
8. Применяем миграции  `python manage.py migrate`
9. Загружаем данные `python manage.py loaddata db.json`
10. Запускаем проект `python manage.py runserver`
