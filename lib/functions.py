from django.core.mail.message import EmailMultiAlternatives
from django.conf import settings
from django.http import (
    Http404, HttpResponse, JsonResponse, HttpResponsePermanentRedirect, HttpResponseRedirect,
)
import time
import requests
import math

def send_mail_with_html(subject, html_message, to_email, reply_to, from_email = None):
    if isinstance(to_email, str):
        to = [to_email]
    else:
        to = to_email
    if isinstance(reply_to, str):
        reply_to = [reply_to]

    msg = EmailMultiAlternatives(
        subject=subject,
        from_email=from_email,
        to=to, 
        reply_to=[reply_to]
    )
    msg.attach_alternative(html_message, 'text/html')
    print(msg.send())

def my_login_required(function):
    def wrapper(request, *args, **kw):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/accounts/login')
        else:
            return function(request, *args, **kw)
    return wrapper


def get_mapillary_user(token):
    # omit the bbox if you want to retrieve all data your account can access, it will automatically limit to your subscription area
    url = 'https://a.mapillary.com/v3/me?client_id=' + settings.MAPILLARY_CLIENT_ID
    headers = {"Authorization": "Bearer {}".format(token)}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data

def get_sequence_by_key(token, seq_key):
    if seq_key is None:
        return False
    url = 'https://a.mapillary.com/v3/sequences/{}?client_id={}'.format(seq_key, settings.MAPILLARY_CLIENT_ID)
    headers = {"Authorization": "Bearer {}".format(token)}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data

def distance(origin, destination):
    lon1, lat1 = origin
    lon2, lat2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d

def check_mapillary_token(user, token=None):
    if token is None:
        if user.mapillary_access_token == '' or user.mapillary_access_token is None:
            return False
        map_user_data = get_mapillary_user(user.mapillary_access_token)
    else:
        map_user_data = get_mapillary_user(token)

    if map_user_data is None or 'message' in map_user_data.keys():
        print(map_user_data['message'])
        return False
    else:
        return map_user_data
