from rest_framework.views import APIView
from rest_framework.response import Response
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
        user = authenticate(username=username, password=password)
        print(username)
        if user is not None:
            return Response({'status': True, 'message': 'Admin Approved'})
        else:
            return Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)