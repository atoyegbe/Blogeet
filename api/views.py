from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BlogSerializer, ProfileSerializer
from blog.models import Blog, Profile
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/blog-list/',
        'Detail View':'/blog-detail/<str:pk>/',
        'Create': '/blog-create/',
        'Update':'/blog-update/<str:pk>/',
        'Delete':'/blog-delete/<str:pk>/',
        
        'Profile-List': '/profile-list/',
        'Profile-view': '/profile-detail/<str:pk>',
    }
    
    return Response(api_urls)

@api_view(['GET'])
def blogList(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def blogDetail(request, pk):
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(instance=blog, many=False)
    
    return Response(serializer.data)

@api_view(['POST'])
def blogCreate(request):
    serializer = BlogSerializer(request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['POST'])
def blogUpdate(request, pk):
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(instance=blog, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)


@api_view(['DELETE'])
def blogDelete(request, pk):
    blog = Blog.objects.get(id=pk)
    
    blog.delete()
    
    return Response(serializer.data)
    
@api_view(['GET'])
def profileList(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def profileDetail(request, pk):
    profile = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(instance=profile, many=False)
    
    return Response(serializer.data)

