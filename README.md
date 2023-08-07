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

## Step 3 - Item app, basic migration
* Create new app ```python manage.py startapp item```
* Creating a simple db model
    * In ```/item/models.py``` add the db model
    * Then ```python manage.py makemigrations```
    * Then to implement the migration ```python manage.py migrate```
* Admin dashboard 
    * Create a super user ```python manage.py createsuperuser```
    * To show db table in admin 
        * In ```item/admin.py``` import model and add ```admin.site.register(Category)```
        * Add ```meta``` class and ```__str__``` to override default properties
* Displaying items
    * In ```core/views.py``` import items and return to the html
    * For displaying image
        * Add in settings.py ``` MEDIA_URL = 'media/';
                MEDIA_ROOT = BASE_DIR / 'media'``` 
        * In ```puddle/urls.py``` add 
        <br>
       <code> from django.conf import settings ;from django.conf.urls.static import static </code>
       <br>
       <br>

            <code>  urlpatterns = [
            path('', index, name='index'),
            path('contact/', contact, name='contact'),
            path('admin/', admin.site.urls),
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) </code>

## Step 4 - Adding detailed items
* Adding custom urls for each apps
* Adding links like ```href="{% url 'core:contact' %}"```

## Step 5 - Sign up form
* Creating ```/core/forms.py``` to handle sigup using userCreation form and user model
* Register this route in ```/core/views.py``` get and post routes, and update ```/core/urls.py```
* Add ```template/core/signup.html```

## Step 6 - Login form
* Setting up login functionalities in ```/core/forms.py```
* Register login in ```/core/urls.py```
* Add ```/core/templates/core/login.html``` similar to signup.html
* Give default login redirections, logout redirection and login url in ```puddle/settings.py``` 

## Step 7 - Adding new items
* Setting entering new items using forms ```/item/forms.py```
* Register this in ```/item/urls.py```
* Add post request handling in ```/item/views.py```
* Add ```templates/item/form.html```     

## Step 8 - Creating a dashboard
* Create new app ```python3 manage.py startapp dashboard```, then regsister this in settings.py
* Create index function in ```dashboard/views.py``` and register this in ```dashboard/urls.py```
* Create ```templates/dashboard/index.html``` 

## Step 9 - Deleting items
* Modify ```item/views.py``` and ```templates/item/details.html```

## Step 10 - Editing items
* Modify ```item/views.py``` and ```templates/item/details.html```

## Step 11 - Search functionality
* Add new function in ```item/views.py``` then update in ```template/item/items.html```, ```urls.py```

## Deployment
* Change in ```settings.py``` and check the deployment using ```python manage.py check --deploy```
* Then mmigrate the db
