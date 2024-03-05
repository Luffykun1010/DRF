from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import *
from django.contrib.auth import login,authenticate
class LoginView(APIView):
    def get(self, request):
        user =  User.objects.all()
        serializer = LoginSerializer(user,many = True)
        return Response(serializer.data)
    def post(self, request):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)
        if User.objects.filter(username=username).exists():
            print('Already Exists')
            # user = authenticate(username=username,password=password)
            # user = User.objects.get(username=username)
            # if user is not None:  
            #     print('Logged in')
            #     login(request,user)
            return Response({'error': 'Username already exists'}, status=status.HTTP_200_OK)
        else:
            serializer = LoginSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                print('Successfully Created')
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)