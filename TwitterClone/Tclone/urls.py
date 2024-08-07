
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('profile/<str:pk>', views.profile, name="profile"),
    path('profile_settings',views.profile_settings, name='profile_settings'),
    path('register', views.register, name="register"),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('profile_list',views.profile_list, name='profile_list'),
    path('bolt_like/<str:pk>',views.bolt_like, name="bolt_like"),
    path('bolt_share/<str:pk>',views.bolt_share, name="bolt_share"),
    path('search', views.search, name='search'),
    path('delete_bolt/<str:pk>', views.delete_bolt, name='delete_bolt'),
]