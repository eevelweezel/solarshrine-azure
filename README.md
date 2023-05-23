# solar_shrine
Website for the Solar Shrine project... new and improved.

## To run
I'm going to assume you have python & docker installed and configured.
If not, please go fix that.
This is a dockerized Django project, currently targeting Python 3.11.  To get started, create an env file.

### install requirements
pip install -r requirements.txt

### run collectstatic
python manage.py collectstatic

### run migrations
python manage.py migrate

### run the dev server:
python manage.py runserver

### build the container
docker build -t solar .

### run the container
docker run solar
