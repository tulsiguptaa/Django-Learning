from django.urls import path
from .views import send_email,send_email_msg, bulk_email

urlpatterns = [
    path('send-email/', send_email, name="send_email"),
    path('send-email-msg/', send_email_msg, name="send_email_msg"),
    path('bulk-email/', bulk_email, name="bulk_email"),
]
