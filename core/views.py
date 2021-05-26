# core/views.py
from django.shortcuts import render, redirect

from .forms import PostForm
from .models import Post


def post(request):
    # if this is a POST request then process the data
    if request.method == 'POST':
        # create and populate a form instance with the data coming for the POST request
        form = PostForm(request.POST)
        # The `is_valid` method returns True if there is data 
        # in the form and the form contains no errors 
        if form.is_valid():
            # create a post instance
            post = Post()
            # We get the data from the `cleaned_data` attribute,
            # write it to the `Post` model, and save
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.activate = form.cleaned_data['activate']
            post.author = form.cleaned_data['author']
            post.email = form.cleaned_data['email']
            post.save()
            
            # redirect to the home page
            return redirect('home')
        
    # if this is a GET or other request create a blank form
    else:
        form = PostForm()
    
    # We render the post page to create a post or
    # to correct errors if there are any
    return render(request, 'post.html', {'form': form})