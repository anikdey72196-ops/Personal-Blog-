from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Blog, Profile
from django.utils import timezone

def add_Blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        date = request.POST.get('date') or timezone.now().date()
        blog = Blog(title=title, content=content, date=date)
        blog.save()
        return redirect('dashboard')

    return render(request, 'article/blog_form.html')

def edit_Blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        blog.title = request.POST.get('title')
        blog.content = request.POST.get('content')
        date_str = request.POST.get('date')
        if date_str:
            blog.date = date_str
        blog.save()
        return redirect('dashboard')
    return render(request, 'article/blog_form.html', {'blog': blog})

def delete_Blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('dashboard')
    return render(request, 'article/delete_blog.html', {'blog': blog})
