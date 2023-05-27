from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from rest_framework.response import Response
# Create your views here.


@login_required
def index(request):
    return render(request, 'index.html', {})


def login_html(request):
    return render(request, 'login.html', {})




def main_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        return redirect('login')

def login_api(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(username, password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    else:
        return HttpResponseBadRequest('Geçersiz istek yöntemi.')


@login_required  
def logout_view(request):
    # Kullanıcıyı oturumdan çıkış yaptır
    logout(request)
    
    # İsteğe JSON yanıtı döndür
    return redirect('login')
