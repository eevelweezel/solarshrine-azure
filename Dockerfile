FROM python:3.11-slim-bookworm

RUN apt-get -y update \
    && apt-get -y upgrade \
    && apt-get -y install git libjpeg-dev zlib1g-dev libpq-dev gcc


WORKDIR /opt/app

COPY . .
# try w/o venv...
#RUN python -m venv venv \
#    && venv/bin/pip install --upgrade pip setuptools wheel \
#    && venv/bin/pip install --no-cache-dir -r requirements.txt \
#    && source venv/bin/activate
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt


ENV PATH="$PATH:/opt/app"
ENV PYTHONPATH=.

EXPOSE 8000

#CMD python manage.py runserver
ENTRYPOINT ["gunicorn", "--bind", ":8000", "solar.wsgi:application"]
