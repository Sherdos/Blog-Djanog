from django.urls import path
from post.views import index, post, contact, about, category_filter

urlpatterns = [
    
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact', contact, name='contact'),
    path('post/', post, name='post'),
    path('category/<int:cat_id>/', category_filter, name='category'),
]