from django.shortcuts import render
import stripe
from .models import Item
from django.http import HttpResponse

stripe.api_key = "sk_test_51MZt18II8Ne1sge3CjGUHR0jQCa7sscZxcgbQ76pBwYwCxDTeXPOIA0rgx8Qq38fXm4cm6Nle52kV2a15VFlzuxC00AKQeGL3i"


def get_stripe_session(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        return HttpResponse(str({}))
    session = stripe.checkout.Session.create(
        line_items=[
            {
                'price': item.price,
                'quantity': 1
            }
        ],
        mode='payment',
        success_url=f"http://localhost:8000/success/{item_id}",
        cancel_url="http://localhost:8000/cancel/",
    )
    return HttpResponse(str(session))


def get_buy_button(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
        price = stripe.Price.retrieve(item.price)
        item.number_price = price["unit_amount"] / 100
        return render(request, template_name="buy.html", context={"item": item})
    except Item.DoesNotExist:
        return render(request, template_name="error.html")


def on_cancel(request):
    return render(request, template_name="cancel.html")


def on_success(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
        return render(request, template_name="success.html",
                      context={"item": item})
    except Item.DoesNotExist:
        return render(request, template_name="error.html")
