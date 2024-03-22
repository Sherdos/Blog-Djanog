from django.shortcuts import render
from post.models import Post, Category
# Create your views here.
 
def index (request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {
        'posts':posts,
        'categories':categories,
        'title':'Главная'
    }
    return render(request, 'index.html',context)

def category_filter (request, cat_id):
    categories = Category.objects.all()
    cat = Category.objects.get(id=cat_id)
    posts = Post.objects.filter(category_id = cat_id)
    context = {
        'posts':posts,
        'categories':categories,
        'title':cat.title
    }
    return render(request, 'index.html',context)
 
def about (request):
    categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return render(request, 'about.html', context)
 
def contact (request):
    categories = Category.objects.all()
    
    context = {
        'categories':categories
    }
    return render(request, 'contact.html', context)
 
def post (request):
    categories = Category.objects.all()
    
    context = {
        'categories':categories
    }
    return render(request, 'post.html', context)