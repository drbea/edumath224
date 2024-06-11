from django.urls import path

from api import views

# app_name = 'api'

urlpatterns = [
    path('hello/', views.HelloWorld.as_view(), name='hello'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('register/', views.register_user, name='register'),
     path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    # path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    # path('lougout/', views.LogoutAPIView.as_view(), name='logout'),
]