from django.shortcuts import render, redirect
from .models import Post, Subscriber
from .forms import PostForm, SubscriberForm
from django.contrib.auth.decorators import login_required

def index(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SubscriberForm()
    return render(request, 'blog/index.html', {'posts': posts, 'form': form})

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})

@login_required
def manage_subscribers(request):
    subscribers = Subscriber.objects.all()
    return render(request, 'blog/manage_subscribers.html', {'subscribers': subscribers})



