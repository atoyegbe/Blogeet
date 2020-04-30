from django.urls import path
from .views import *

urlpatterns = [
    path('', apiOverview, name="api-overview"),
    path('blog-list/', blogList, name="blog-list"),
    path('blog-detail/<str:pk>/', blogDetail, name='blog-detail'),
    path('blog-create/', blogCreate, name="blog-create"),
    path('blog-update/<str:pk>/', blogUpdate, name="blog-update"),
    path('blog-delete/<str:pk>/', blogDelete, name="blog-delete"),
    
    path('profile-list/', profileList, name="profile-list" ),
    path('profile-detail/', profileDetail, name="profile-detail" ),
]
