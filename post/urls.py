from django.urls import path
from post.views import index, post, contact, about, category_filter, post_show, add_post, update_post, delete_post

urlpatterns = [
    
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact', contact, name='contact'),
    path('post/', post, name='post'),
    path('category/<int:cat_id>/', category_filter, name='category'),
    path('post/<int:id>/', post_show, name='post_show'),
    path('post/add/', add_post, name='post_add'),
    path('post/update/<int:id>/', update_post, name='post_update'),
    path('post/delete/<int:id>/', delete_post, name='post_delete'),
]