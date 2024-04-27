from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def set_session(request):
    request.session['username'] = 'lehya'
    return HttpResponse("session data set!")
def get_session(request):
    username = request.session.get('username','Guest')
    return HttpResponse(f"Hello, {username} !")