from django.shortcuts import render, redirect
from post.models import Post, Category
import random
# Create your views here.
def get_all_totoly_context():
    categories = Category.objects.all()
    
    context = {
        'categories':categories
    }
    return context
 
def index (request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
        'title':'Главная'
    }
    context.update(get_all_totoly_context())
    # context = {**context, **get_all_totoly_context()}
    return render(request, 'index.html',context)

def category_filter (request, cat_id):
    cat = Category.objects.get(id=cat_id)
    posts = Post.objects.filter(category_id = cat_id)
    context = {
        'posts':posts,
        'title':cat.title
    }
    context.update(get_all_totoly_context())
    return render(request, 'index.html',context)
 
def about (request):
    context = {
        'title':'О нас'
    }
    context.update(get_all_totoly_context())
    return render(request, 'about.html', context)

 
def post (request):
    posts = Post.objects.all()
    post = random.choice(posts)
    context = {
        'title':'Лета',
        'post':post
    }
    context.update(get_all_totoly_context())
    return render(request, 'post.html', context)

def post_show(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post':post
    }
    context.update(get_all_totoly_context())    
    return render(request, 'post_show.html', context)

def add_post(request):
    title = request.POST.get('title')
    descrition = request.POST.get('description')
    image = request.FILES.get('image')
    category = request.POST.get('category')
    if category == 'None':
        category = None
    Post.objects.create(title=title, descrition=descrition, image=image, category_id=category)
    return redirect('index')


def update_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        title = request.POST.get('title')
        descrition = request.POST.get('descrition')
        category = request.POST.get('category')
        post.title = title
        post.descrition = descrition
        post.category_id = category
        post.save()
        return redirect('post_show', id)
    context = {
        'post':post
    }
    context.update(get_all_totoly_context())    
    
    return render(request, 'post_update.html', context)

def delete_post (request, id):
    Post.objects.get(id=id).delete()
    
    return redirect('index')
 
 
def search_post(request):
    key = request.POST.get('key')
    posts = Post.objects.filter(title=key)
    context = {
        'posts':posts
    }
    
    context.update(get_all_totoly_context())   
    return render(request, 'index.html', context)

def add_like(request):
    post_id = request.POST.get('id')
    post = Post.objects.get(id=post_id)
    post.count_like +=1
    post.save()
    
    return redirect('post_show', post_id)