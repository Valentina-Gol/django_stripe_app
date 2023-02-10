# django-stripe app

## How to run it?
You need to set up environment (just once)
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r py_requirements.txt

```

Then you need to run the server
```
cd django_stripe
python3 manage.py runserver

```

## Info
Server start on http://localhost:8000

Available urls:
```
/buy/<int:item_id>/  
/item/<int:item_id>/  
/cancel/  
/success/<int:item_id>/
```

## Admin
For adding and deleting objects in database use admin page.
For that create a superuser with Django and go to admin page http://localhost:8000/admin/
```
cd django_stripe
python3 manage.py createsuperuser

```
