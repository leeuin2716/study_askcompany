from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView
from django.shortcuts import render
from .models import Post




post_list = ListView.as_view(model=Post)


# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q','')
#     if q:
#         qs = qs.filter(message__icontains=q)
        
#     # instagram/templates/instagram/post_list.html
#     return render(request, 'instagram/post_list.html',{
#         'post_list':qs,
#         'q':q,
#     })        


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    response = HttpResponse()
    response.write("Hello Word")
    return response