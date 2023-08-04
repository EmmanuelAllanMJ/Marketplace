# Django Project setup

## Step 1 - setup app
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

## Step 2 - Frontend setup
Rendering basic html page
* Under ```/core/views.py```, define function to render the page
* Under ```/core/templates/core``` we will create all our html page
* In ```/puddle/urls.py``` we reserve these routes which we defined in views.py

