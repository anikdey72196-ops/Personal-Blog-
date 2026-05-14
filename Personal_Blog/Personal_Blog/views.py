from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from article.models import Profile, Blog

def register(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        conform_password = request.POST.get('conform_password')
        if password == conform_password:
            register_user = Profile(name=user, password=password, email=email, conform_password=conform_password)
            register_user.save()
            return redirect('index') 
        else:
            return HttpResponse("Passwords do not match.")
        
    return render(request, 'register.html')

def index(request):
    blogs = Blog.objects.all().order_by('-date')
    return render(request, 'index.html', {'Blogs': blogs}) 

def article_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'article/article.html', {'blog': blog})

def dashboard(request):
    blogs = Blog.objects.all().order_by('-date')
    return render(request, 'index.html', {'Blogs': blogs, 'is_admin': True})