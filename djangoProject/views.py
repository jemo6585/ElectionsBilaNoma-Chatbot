from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .bot import *
account_sid = "AC25d2a5d33190909b2d86128dc03da95e"
auth_token = "3353dd42da170b5a7089eee19e8117cb"

from twilio.rest import Client

client = Client(account_sid, auth_token)

@csrf_exempt
def main(request):
    try:
        profileName = request.POST['ProfileName']
        sender =request.POST['From']
        msg = request.POST['Body']
        resp = predict_class(msg)
        resp = get_response(resp, intents)

        client.messages.create(
        to=f'{sender}',
        from_='whatsapp:+14155238886',
        body=resp
        )
    except:
        pass
    finally:

        return HttpResponse("Hello")

