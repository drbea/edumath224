from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from .serializers import LoginSerializer


class HelloWorld(APIView):
    def get(self, request):
        return Response({"hello": "Hello, world!, from django"}, status=status.HTTP_200_OK)


class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return Response({'message': 'You are now logged in', 'username': user.username}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Username or password is incorrect'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

