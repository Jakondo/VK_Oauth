# core/views.py
import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from pprint import pprint


# Create your views here.
def login(request):
    is_authorised = request.user.is_authenticated
    if is_authorised:
        return redirect(home)
    else:
        return render(request, 'login.html')


@login_required
def home(request):
    acc_tok = request.user.social_auth.get().extra_data['access_token']
    r = requests.get('https://api.vk.com/method/friends.get', params = {'access_token' : acc_tok, 'order': 'random', 'count': 5, 'v': 5.210, 'fields': 'first_name, last_name, photo_100'})
    friends = r.json()['response']
    pprint(friends)
    return render(request, 'home.html', friends)
