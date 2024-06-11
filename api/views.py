from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from .serializers import LoginSerializer

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authentification.tokens import account_activation_token

@api_view(['POST'])
def register_user(request):
    data = request.data
    username = data.get('username')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    password2 = data.get('password2')

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(email=email).exists():
        return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
    
    if len(username) > 15:
        return Response({'error': 'Username must be under 15 characters'}, status=status.HTTP_400_BAD_REQUEST)
    
    if password != password2:
        return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

    if not username.isalnum():
        return Response({'error': 'Username must be alphanumeric'}, status=status.HTTP_400_BAD_REQUEST)
    
    new_user = User.objects.create_user(username, email, password)
    new_user.first_name = first_name
    new_user.last_name = last_name
    new_user.is_active = False
    new_user.save()
    
    subject = 'Welcome to edumath224'
    message = (
        f"Hello {new_user.username},\n\n"
        "Your account has been created successfully.\n"
        "Thank you for using edumath224.\n"
        "We have sent you a confirmation email. Please confirm your email address to activate your account.\n\n"
        "Thank you,\nedumath224 team"
    )
    from_email = settings.EMAIL_HOST_USER
    to_list = [email]
    send_mail(subject, message, from_email, to_list, fail_silently=False)

    current_site = get_current_site(request)
    email_subject = 'Activate your account for edumath224'
    message2 = render_to_string('authentification/email_confirmation.html', {
        'name': new_user.username,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
        'token': account_activation_token.make_token(new_user),
    })
    email = EmailMessage(email_subject, message2, settings.EMAIL_HOST_USER, [email])
    email.fail_silently = True
    email.send()
    
    return Response({'message': 'User registered successfully, please check your email to activate your account'}, status=status.HTTP_201_CREATED)


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



def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your account has been confirmed.')
        return redirect('authentification:login')
    else:
        return render(request, 'authentification/activation_failed.html')

