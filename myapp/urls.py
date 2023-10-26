from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user.authenticate, name='login'),
    path('signup/', views.user.signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
]