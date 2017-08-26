from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings

from twilio.rest import Client
import logging

# Twilio configuration variables
twilio_account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
twilio_auth_token  = "your_auth_token"

# client = Client(twilio_account_sid, twilio_auth_token)
#
# message = client.messages.create(
#     to="+15558675309",
#     from_="+15017250604",
#     body="Hello from Python!")
#
# print(message.sid)


# csrf exempt request to allow POST request
@csrf_exempt
def index(request):
    return HttpResponse("<pre>Not found.</pre>")

@csrf_exempt
def send_number(request):
    if request.method != 'POST':
        return HttpResponse("Request must be POST request.")
    return HttpResponse("send_number endpoint.")

@csrf_exempt
def verify_code(request):
    if request.method != 'POST':
        return HttpResponse("Request must be POST request.")
    return HttpResponse("verify_code endpoint.")
