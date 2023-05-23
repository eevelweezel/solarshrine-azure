FROM python:3.11.3-slim-bullseye

RUN apt-get -y update \
    && apt-get -y upgrade \
    && apt-get -y install git libjpeg-dev zlib1g-dev libpq-dev gcc

WORKDIR /opt

RUN git clone https://github.com/eevelweezel/solarshrine-azure.git

WORKDIR /opt/solarshrine-azure

RUN set -e \
    && python -m venv /venv \
    && /venv/bin/pip install --upgrade pip setuptools wheel \
    && /venv/bin/pip install --no-cache-dir -r requirements.txt

ENV PATH="$PATH:/opt/venv/bin"
ENV PYTHONPATH=.

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "1", "solar.wsgi:application"]
