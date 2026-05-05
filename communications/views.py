from django.shortcuts import render
import requests
from config.settings.base import WEBHOOK_URL



# Create your views here.
def index(request):
    if request.method == "POST":
        message = request.POST.get("message")

        data = {
            "content": f"**Transmission Received:**\nMessage: {message}"
        }

        requests.post(WEBHOOK_URL, json=data)

    return render(request, "communications/index.html")

