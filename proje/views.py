from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
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

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def login_html(request):
    return render(request, 'login.html', {})


from django.http import HttpResponseRedirect

from rest_framework.response import Response

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(username, password)
            return Response({'redirect_url': reverse('index')})
        else:
            print(username, password, "else")
            return Response({'redirect_url': reverse('login_html')})
    else:
        print("post değil")

        



