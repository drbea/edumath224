from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
# from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string

from .tokens import account_activation_token

from config import settings


# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        print(username, email, password)

        if User.objects.filter(username=username):
            messages.error(request, 'username already exists')
            return redirect("home:home")
        
        if User.objects.filter(email=email):
            messages.error(request, 'email already exists')
            return redirect("home:home")

        if len(username) > 15:
            messages.error(request, 'username must be under 15 characters')
            return redirect("home:home")

        if password == password2:
            if not username.isalnum():
                messages.error(request, 'username must be alpha numeric')
                return redirect("home:home")
            print('password matched')
            new_user = User.objects.create_user(username, email, password)
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.is_active = False
            new_user.save()
            
            print('user created')
                        
            # welcome email
            subject = 'welcome to edumath224'
            message = (
                f"Hello {new_user.username},\n\n"
                "Your account has been created successfully.\n"
                "Thank you for using edumath224.\n"
                "We have sent you a confirmation email. Please confirm your email address to activate your account.\n\n"
                "Thank you,\nedumath224 team"
            )
            from_email = settings.EMAIL_HOST_USER
            to_list = [email]
            try:
                send_mail(subject, message, from_email, to_list, fail_silently=False)
                print("Email sent successfully")
            except Exception as e:
                print(f"Error sending email: {e}")
            
            messages.success(request, 'your account has been created successfully we have sent you a confirmation email please confirm your email address to activate your account')
            
            
            # email verification
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
            # from_email = settings.EMAIL_HOST_USER
            # to_list = [email]
            try:
                email.send()
                # send_mail(email_subject, message2, from_email, to_list, fail_silently=False)
                print("confirmation Email sent successfully")
            except Exception as e:
                print(f"Error sending confirmation email: {e}")
            
            return redirect('authentification:login')
        else:
            print('password not matched')
            messages.error(request, 'password not matched')
            
    
    return render(request, 'authentification/register.html')


def login_user(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            messages.success(request, 'you are now logged in')
            login(request, user)
            context = {
                'fname': user.username
            }
            return render(request, 'home/index.html', context)
        else:
            messages.error(request, 'username or password is incorrect')
            return redirect('authentification:login')

    return render(request, 'authentification/signup.html')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        new_user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        new_user = None

    if new_user is not None and account_activation_token.check_token(new_user, token):
        new_user.is_active = True
        new_user.save()
        login(request, new_user)
        messages.success(request, 'your account has been activated')
        return redirect('home:home')
    else:
        messages.error(request, 'activation link is invalid')
        # return redirect('authentification:login')
        return render(request, 'authentification/activation_invalid.html')
    


def logout_user(request):

    logout(request)
    messages.success(request, 'you have been logged out')
    return render(request, 'home/index.html')