from django import forms
from .models import Post
import re

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = [
            'message','photo','tag_set','is_public'
        ]
        # exclude = []   # 어떠한 필드를 배제 하겠다 
        
        
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if message:
            message= re.sub(r'[a-zA-Z]+','',message)
            
        return message
            
        