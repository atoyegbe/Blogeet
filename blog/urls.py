from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<str:pk>/', views.blogs, name='blog'),
    
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name="login"),
    path('logout', views.logoutPage, name="logout"),
    
    path('profile/', views.profilePage, name='profile'),
    path('account_settings/', views.profileSetting, name="settings"),
    
    path('deletePost/<str:pk>/', views.deletePost, name="delete_post"),
    path('create_blog/', views.create_blog, name='create_blog'),
]

