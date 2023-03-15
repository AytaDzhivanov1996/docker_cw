import requests
from django.conf import settings
from rest_framework.response import Response


def send_message(text):
    data_for_request = {
        "chat_id": f"{settings.TELEGRAM_CHAT_ID}",
        "text": text
    }
    response = requests.get(f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage',
                            data_for_request)
    return Response(response.json())
