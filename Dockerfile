FROM python:3.11.3-slim-bullseye

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y git libjpeg-dev zlib1g-dev libpq-dev gcc\
   && rm -rf /var/lib/apt/lists/*

RUN set -e \
    && python3 -m venv /opt/venv

WORKDIR /opt

RUN git clone https://github.com/eevelweezel/solarshrine-azure.git

WORKDIR /opt/solarshrine-azure

RUN pip install -U pip setuptools wheel

RUN set -e \
    && pip install -r requirements.txt

ENV PATH="/opt/venv/bin:${PATH}"

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "1", "solar.wsgi:application"]

