from django.contrib import admin
from django.urls import path
from .views import get_stripe_session, get_buy_button, on_cancel, on_success

urlpatterns = [
    path('admin/', admin.site.urls),
    path('item/<int:item_id>/', get_stripe_session),
    path('buy/<int:item_id>/', get_buy_button),
    path('cancel/', on_cancel),
    path('success/<int:item_id>/', on_success)
]
