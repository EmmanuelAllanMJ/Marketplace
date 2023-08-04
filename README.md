# Django Project setup

- Create venv
```python3 -m venv venv```
- Go into venv 
```source ./venv/bin/activate```
- Install django
``` pip install django```

- Create new project
```django-admin startproject puddle```

- Running django server 
```python manage.py runserver```

- Create frontend app
```python manage.py startapp core```
    - Add core in ```/settings.py``` INSTALLED_APPS