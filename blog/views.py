from django.shortcuts import render, redirect
from .models import *
from .forms import createBlog, CreateUserForm, profileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



from .decorators import unauthenticated_user, allowed_user, admin_only



# Create your views here.
def home(request):
    blog_posts = Blog.objects.all()
    context = {'blog_posts': blog_posts}
    template_name = 'blog/homepage.html'
    
    return render(request, template_name, context)

def blogs(request, pk):
    blog = Blog.objects.get(id=pk)
    
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
    users = request.user.profile
    form = profileForm(instance=users)
    
    if request.method == 'POST':
        form = profileForm(request.POST, request.FILES, instance=users)
        if form.is_valid():
            form.save()
    
    template_name = 'blog/user_page.html'
    context = {'form': form}
    return render(request, template_name, context)       
            
@login_required(login_url='login')
def deletePost(request, blog_id):
    template_name = 'blog/delete.html'
    
    blog_post = Blog.objects.get(id=blog_id)
    if request.method == 'POST':
        blog_post.delete()
        return redirect('home')
        
    context = {"blog_post": blog_post}
    
    return render(request, template_name, context)

@login_required(login_url='login')
def create_blog(request):
    template_name = 'blog/create_blog.html'
    blog_form = createBlog()
    
    if request.method == 'POST':
        blog_form = createBlog(request.POST)
        if blog_form.is_valid():
            blog_form.save()
            return redirect('home')
    
    context = {'blog_form': blog_form}
    
        
    return render(request, template_name, context)
