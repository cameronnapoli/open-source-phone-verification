# open-source-phone-verification
Open source phone verification software using Django and Twilio. Currently using SQLite for database, but this can be configured in phone_verif_proj/settings.py.


### Usage
This code is not intended to be a full implementation of a phone verification system. Instead, it functions as an example of phone verification code that can be easily integrated into an existing Django project.

### Prerequisites
Python version 3.5.2

### Dependencies
Django v1.8.18

twilio v6.4.1

### Run server
cd into repo directory, and run Django server with:
```
python manage.py makemigrations phone_verif
python manage.py migrate
python manage.py sqlmigrate phone_verif 0001
python manage.py runserver
```
