# core/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
from pprint import pprint


# Create your views here.
def login(request):
    return render(request, 'login.html')


@login_required
def home(request):
    acc_tok = request.user.social_auth.get().extra_data['access_token']
    r = requests.get('https://api.vk.com/method/friends.get', params = {'access_token' : acc_tok, 'count': 5, 'v': 5.210, 'fields': 'first_name, last_name, photo_100'})
    friends = r.json()['response']
    pprint(friends)
    return render(request, 'home.html', friends)
