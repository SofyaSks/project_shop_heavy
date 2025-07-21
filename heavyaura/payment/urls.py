from django.urls import path
from . import views, webhooks

app_name = 'payment'

urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('completed/', views.payment_completed, name='completed'),
    path('cancled/', views.payment_cancled, name='cancled'),
    path('webhook/', views.payment_webhook, name='webhook'),
]