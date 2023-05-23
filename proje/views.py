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

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def login_html(request):
    return render(request, 'login.html', {})


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(username,password)
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({'token': str(token)}, status=200)
            return redirect('index')
        else:
            print(username,password,"else")
            return redirect('login_html')
    else:
        print("post değil")
        



