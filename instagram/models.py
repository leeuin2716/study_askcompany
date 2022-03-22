from django.db import models
from django.conf import settings
from util.views import uuid_name_upload_to
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    photo = models.ImageField(blank =True, upload_to = uuid_name_upload_to)
    tag_set = models.ManyToManyField('Tag', blank=True)
    is_public = models.BooleanField(default=False,verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    # javadml toString
    def __str__(self):
        # return f"Custom Post object ({self.id})"
        return self.message
    def get_absolute_url(self):
        return reverse('instagram:post_detail',args=[self.pk])
    
    
    
    def message_length(self):
        return f"{len(self.message)}글자"
    message_length.short_description = "메세지 글자수"
    
    class Meta:
        ordering = ['-id']
        
        
        
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             limit_choices_to={'is_public':True})
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # post_set = models.ManyToManyField(Post)
    
    def __str__(self):
        return self.name