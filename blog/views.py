from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import generic
from django.utils import timezone

from .forms import createBlog, CreateUserForm, profileForm, SuggestionForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_user, admin_only


# Create your views here.
def home(request):
    blog = Blog.objects.all()
    blog_posts = blog.filter(
            date_posted__lte=timezone.now()
            ).order_by('-date_posted')[:5]
    

    
    context = {'blog_posts': blog_posts }
    template_name = 'blog/homepage.html'
    
    return render(request, template_name, context)


def blogs(request, pk):
    blog = Blog.objects.get(id=pk)
    # blog = get_object_or_404(Blog, slug=slug)
    
    context = {'blog': blog}
    template_name = 'blog/blog.html'
    
    return render(request, template_name, context)

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form =  CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            messages.success(request, f'Account was created succesfully')
            return redirect('login')
    
    context = {'form': form}
    return render(request, 'blog/register.html', context)
    
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username OR password is incorrect')
    
    context = {}
    return render(request, 'blog/login.html', context)

@login_required(login_url='login')
def logoutPage(request):
     logout(request)
     
     return redirect('login')

@login_required(login_url='login')
def profilePage(request):
    blogs = Blog.objects.filter(creator=request.user, date_posted__lte=timezone.now()).order_by('-date_posted')
    form = profileForm()
    if request.method == 'POST':
        form = profileForm(request.POST, request.FILES, instance=users)
        if form.is_valid():
            form.save()
    
    template_name = 'blog/user_page.html'
    context = {'form': form , 'blogs' : blogs}
    return render(request, template_name, context)       
            
@login_required(login_url='login')
def deletePost(request, pk):
    template_name = 'blog/delete.html'
    
    blog_post = Blog.objects.get(id=pk)
    if request.method == 'POST':
        blog_post.delete()
        return redirect('home')
        
    context = {"blog_post": blog_post}
    
    return render(request, template_name, context)

@login_required(login_url='login')
def profileSetting(request):
    users = request.user.profile
    form = profileForm(instance=users)
    
    if request.method == 'POST':
        form = profileForm(request.POST, request.FILES, instance=users)
        if form.is_valid():
            form.save()
            return redirect('profile')
    
    template_name = 'blog/account_setting.html'
    context = {'form': form}
    return render(request, template_name, context) 
    

@login_required(login_url='login')
def create_blog(request):
    template_name = 'blog/create_blog.html'
    form = createBlog()
    
    if request.method == 'POST':
        form = createBlog(request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.creator = request.user
            new_blog.save()
            return redirect('home')
    
    context = {'form': form}
    
        
    return render(request, template_name, context)

