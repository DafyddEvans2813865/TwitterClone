
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('profile/<str:pk>', views.profile, name="profile"),
    path('profile_settings',views.profile_settings, name='profile'),
    path('register', views.register, name="register"),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
        path('profile_list',views.profile_list, name ='profile_list')

]