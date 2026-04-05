from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post

def blog(request):
	return render(request,'blog.html')


# 🔐 Blog page
@login_required
def blog_home(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {"posts": posts})


# ℹ️ About page (no login needed)
def about(request):
    return HttpResponse("This is about page 😄")


# ➕ Add Post
@login_required
def add_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES.get("image")

        Post.objects.create(title=title, content=content, image=image)

        return redirect('/blog/')

    return render(request, 'form.html')

# ❌ Delete Post
@login_required
def delete_post(request, index):
    post = Post.objects.get(id=index)
    post.delete()
    return redirect('/blog/')


# ✏️ Edit Post
@login_required
def edit_post(request, index):
    post = Post.objects.get(id=index)

    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.save()
        return redirect('/blog/')

    return render(request, 'edit.html', {"post": post})



def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists ❌")
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Account created successfully ✅")
            return redirect('/login/')

    return render(request, 'signup.html')