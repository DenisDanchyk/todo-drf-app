## Setup
### 1. Install Python3 interpreter
Additional information on https://www.python.org/downloads/

### 2. Clone this repository into your directory

    mkdir todo-app && cd todo-app
    git clone https://github.com/DenisDanchyk/todo-drf-app.git .
    
### 3. Create virtual environment

    python -m venv venv
    venv\scripts\activate.bat

### 4. Install requirements
    
    cd core
    pip install -r requirements.md

### 5. Set you Google account credentials for sending email system
    In `core/settings.py` add your Google account credentials to `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD`. If you don't have Google account - <a href="https://accounts.google.com/signup">create it</a>. Alternitavely, you can use other SMTP host.
    Instructions, how to set Django SMTP described 
    <a href="https://medium.com/@_christopher/how-to-send-emails-with-python-django-through-google-smtp-server-for-free-22ea6ea0fb8e">here</a>.
    
    
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    # TODO :
    EMAIL_HOST_USER = ""
    EMAIL_HOST_PASSWORD = ""
    
### 6. Create PosgresSQL database in a way convenient for you
    
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

### 7. Make migrations and run server
    python manage.py makemigrations 
    python manage.py migrate 
    python manage.py runserver
