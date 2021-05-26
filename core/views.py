# core/views.py
from django.shortcuts import render, redirect

from .models import Post
from  .forms import PostForm

def post(request):
    form = PostForm()
    return render(request, 'post.html', {'form': form})