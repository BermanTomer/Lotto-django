# Lotto-django
Import CSV file of the lotto result from Israel lotto server.
- convert format from Hebrew to English
- working on the must updating data 
- Display all of the results that drawn more than once

##############
python manage.py startapp Lotto

####When changing Models.py running both of this functions
python manage.py makemigrations
python manage.py migrate

http://127.0.0.1:8000
