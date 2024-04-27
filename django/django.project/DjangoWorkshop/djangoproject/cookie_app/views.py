#from django.shortcuts import render
from django.http import HttpResponse
def set_cookie(____):
    response = HttpResponse("COOKIE SET1")
    response.set_cookie('username', 'Lehya')

    return response

def get_cookie(request):  
    username = request.COOKIES.get('username','Guest')
    return HttpResponse(f"Hello, {username} !")

