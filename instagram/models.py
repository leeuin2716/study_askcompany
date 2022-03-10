from django.db import models
from util.views import uuid_name_upload_to


class Post(models.Model):
    message = models.TextField()
    photo = models.ImageField(blank =True, upload_to = uuid_name_upload_to)
    is_public = models.BooleanField(default=False,verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    # javadml toString
    def __str__(self):
        # return f"Custom Post object ({self.id})"
        return self.message
    
    def message_length(self):
        return f"{len(self.message)}글자"
    message_length.short_description = "메세지 글자수"
    
    class Meta:
        ordering = ['-id']