from django.urls import path
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'
urlpatterns = [
    # Login
    # path('login/', login, {'template_name': 'users/login.html'}, name = 'login'),
    path('login/', auth_views.LoginView.as_view(template_name= 'users/login.html'), name = 'login'),

    # Logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
