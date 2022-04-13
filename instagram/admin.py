from django.contrib import admin
from django.utils.safestring import mark_safe

from instagram.forms import PostForm
from .models import Post,Comment,Tag



#admin.site.register(Post)



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','photo_tag','message','message_length','is_public','created_at','updated_at']
    list_display_links = ['message']
    search_fields = ['message']    
    list_filter = ['created_at','is_public']
    # form = PostForm

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src = "{post.photo.url}" style="width:75px; height:75px;"  />')
        return None
    
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass