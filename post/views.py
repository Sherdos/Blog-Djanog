from django.shortcuts import render
from post.models import Post
# Create your views here.
 
def index (request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'index.html',context)
 
def about (request):
    return render(request, 'about.html')
 
def contact (request):
    return render(request, 'contact.html')
 
def post (request):
    return render(request, 'post.html')