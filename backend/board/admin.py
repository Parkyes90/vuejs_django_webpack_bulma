from django.contrib import admin
from .models import Post
# from .models import Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'create_date')
    list_posts = ('title', 'id', 'modify_date')
    list_filter = ('modify_date',)
    search_fields = ('title', 'content')


# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('message', 'user', 'create_date')


admin.site.register(Post, PostAdmin)
# admin.site.register(Comment)
