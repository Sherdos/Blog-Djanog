from django.contrib import admin
from post.models import Post, Category
# Register your models here.
admin.site.register(Category)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = ('title','created', 'category')
    list_filter = ('category',)
    readonly_fields = ('created',)
    search_fields = ('title',)