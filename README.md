# solar_shrine
Website for the Solar Shrine project

## To run
I'm going to assume you have python 3.7 installed and configured.
If not, please go to https://python.org/downloads and fix that.
This is a django site.  To get started, create a database and update the connection information in settings.py.

### install requirements
pip install -r requirements.txt

### run collectstatic
python manage.py collectstatic

### run migrations
python manage.py migrate

### run the dev server:
python manage.py runserver
