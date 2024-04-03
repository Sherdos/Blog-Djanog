from django.urls import path
from post.views import (index, post, about, 
category_filter, post_show, add_post, 
update_post, delete_post, search_post,add_like, 
add_comment)

urlpatterns = [
    
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('post/', post, name='post'),
    path('category/<int:cat_id>/', category_filter, name='category'),
    path('post/<int:id>/', post_show, name='post_show'),
    path('post/add/', add_post, name='post_add'),
    path('post/update/<int:id>/', update_post, name='post_update'),
    path('post/delete/<int:id>/', delete_post, name='post_delete'),
    path('post/search/', search_post, name='post_search'),
    path('post/add/like/', add_like, name='add_like'),
    path('post/add/comment/', add_comment, name='add_comment'),
]