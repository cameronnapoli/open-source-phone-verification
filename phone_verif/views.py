"""
views.py
Written by: Cameron Napoli
"""

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import VerificationRequestEntry
from random import choice
from twilio.rest import Client
from . import twilio_config


# helper functions
def generate_code(length=4, alphabet='0123456789'):
    ''' generate verification code.
        can configure length and characters in code '''
    return ''.join([choice(alphabet) for i in range(length)])


def json_error_response(content):
    response = '{"success": 0, "error": "%s"}' % content
    return HttpResponse(response)


def json_success_response():
    response = '{"success": 1}'
    return HttpResponse(response)


@csrf_exempt  # csrf exempt request to allow POST request
def index(request):
    return HttpResponse("Not found.")


# endpoint functions
@csrf_exempt
def send_number(request):
    '''
    response endpoint for the initial verify phone request.

    client must send phone_number in the format twilio requires
    for example, it needs to look like this for US phone number
    +19998881234
      or
    9998881234
    '''
    if request.method != 'POST':
        return json_error_response("Request must be POST request.")
    if 'phone_number' not in request.POST:
        return json_error_response("POST parameter(s) not set.")


    # TODO: add user auth



    # Initialize Twilio Client and variables
    to_number = request.POST['phone_number']
    verification_code = generate_code()
    text_body = "Your verification code is: %s" % verification_code

    try:
        client = Client(twilio_config.twilio_account_sid,
                        twilio_config.twilio_auth_token)

        client.messages.create(
            to=to_number,
            from_=twilio_config.from_number,
            body=text_body)

    except TypeError as te:  # trial version of Twilio creating a strange error
        print("*** Possible Twilio glitch, attempt to continue execution *** ")
    except Exception as e:
        return json_error_response("SMS error: %s" % e)

    # Store verification code
    verif_request_obj = VerificationRequestEntry()
    # TODO: add user from request auth
    # verif_request_obj.user
    verif_request_obj.phone_number = to_number.strip(' \n')
    verif_request_obj.verification_code = verification_code.strip(' \n')
    verif_request_obj.save()

    print("Verification code stored (phone_number, code) : (%s, %s)" %
          (to_number, verification_code))
    return json_success_response()


@csrf_exempt
def verify_code(request):
    '''
    response endpoint for the second request once
    the user receives the verification code through
    SMS. (must pass phone number in the same format
    as it was sent in the send_number request)

    POST parameters:
    phone_number
    verification_code
    '''
    if request.method != 'POST':
        return HttpResponse("Request must be POST request.")
    if 'phone_number' not in request.POST or \
       'verification_code' not in request.POST:
        return json_error_response("POST parameter(s) not set.")


    # TODO: add user auth

    # query to see if entry in verification codes, exist
    #   with both phone_number and verification_code
    query_set = VerificationRequestEntry.objects.filter(
            phone_number=request.POST['phone_number'].strip(' \n')
        ).filter(
            verification_code=request.POST['verification_code'].strip(' \n')
        )

    if len(query_set) > 0:
        print("  *** match found (phone_number, verification_code): (%s, %s)" %
              (request.POST['phone_number'].strip(' \n'),
               request.POST['verification_code'].strip(' \n')))

        # set user verified equal to true

        return json_success_response()
    else:
        return json_error_response('Verification code for provided '
                                   'phone number not found.')
