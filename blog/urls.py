from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/', views.blogs, name='blog'),
    
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name="login"),
    path('logout', views.logoutPage, name="logout"),
    
    path('deletePost/<str:blog_id>', views.deletePost, name="delete_post"),
    path('create_blog/', views.create_blog, name='create_blog'),
]

