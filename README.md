# Django-Stripe App

## How to run it?

### Run in docker

```
docker-compose build
docker-compose up -d
```

### Local testing
You need to set up environment (just once)
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r django_stripe/py_requirements.txt
```

Then you need export env variables and run the server
```
export $(grep -v '^#' .env | xargs)
export DOMAIN=localhost:8000
cd django_stripe
python3 manage.py runserver
```

## Info
Server start on http://${DOMAIN}

Available urls:
```
/buy/<int:item_id>/  
/item/<int:item_id>/  
/cancel/  
/success/<int:item_id>/
```

## Admin page
For adding and deleting objects in database use admin page.
For that create a superuser with Django and go to admin page http://${DOMAIN}/admin/
```
cd django_stripe
python3 manage.py createsuperuser
```
