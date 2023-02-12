FROM python:3.9-alpine

RUN mkdir code
COPY requirements.txt code
WORKDIR code
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . .
RUN python3 manage.py collectstatic --noinput

CMD gunicorn django_stripe.wsgi:application --bind 0.0.0.0:8000