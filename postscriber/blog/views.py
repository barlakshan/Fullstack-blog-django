from django.shortcuts import render
from .models import PostModel

def index(request):
    posts = PostModel.objects.all()
    
    return render(request, 'blog/index.html', {'posts': posts})
