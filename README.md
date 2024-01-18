# Ecommerce (ecommerce website built with Django)

## Steps to install the project:
- To install in the MacOs system, after cloning the project into your machine, you have to create a virtual enviroment:

 ```
  python -m venv (the name of your venv)
 ```

- Next, you have to activate that enviroment:

 ```
  . venv/bin/activate
 ```

- Install the dependecies of the project, using the following command:

 ```
  pip install django django-debug-toolbar django-crispy-forms pillow
 ```

- Then, you run the migrations:

 ```
 python manage.py migrate
 ```

- Finally, you can start the project using the following comand:

 ```
 python manage.py runserver
 ```




