from django.shortcuts import render
from .models import BlogPost
# Create your views here.
def home(request):
    posts = BlogPost.objects.get(pk=1)
    context={
        "post":posts
    }
    return(render(request, 'main/index.html', context))