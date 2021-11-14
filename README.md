## Setup
### 1. Install Python3 interpreter
Additional information on https://www.python.org/downloads/

### 2. Clone this repository into your directory

    mkdir todo-app && cd todo-ap
    git clone https://github.com/DenisDanchyk/todo-drf-app.git .
    
### 3. Create virtual environment

    python -m venv venv
    venv\scripts\activate.bat

### 4. Install requirements
    
    cd core
    pip install -r requirements.md
    
### 5. Create PosgresSQL database in a way convenient for you
    
    And set in `core/settings.py` 
    
    DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'HOST': 'localhost',
          'PORT': '5432',
          # TODO:
          'NAME': "",
          'USER': "",
          'PASSWORD': ""
          }
      }

### 6. Make migrations and run server
    python manage.py makemigrations 
    python manage.py migrate 
    python manage.py runserver
