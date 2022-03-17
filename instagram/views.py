from django.http import Http404, HttpRequest, HttpResponse
from django.views.generic import ListView,DetailView
from django.shortcuts import render,get_object_or_404
from .models import Post



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



# post_list = ListView.as_view(model=Post)



post_list = ListView.as_view(model=Post, paginate_by=10)

# class PostListView(ListView):
#     model = Post
#     paginate_by = 10
# post_list = PostListView.as_view()


# class PostListView(ListView):
#     model = Post
#     paginate_by = 10

#     def get_queryset(self):
#         qs = super().get_queryset()
#         qs = qs.filter(...)
#         return qs

# post_list  =  PostListView.as_view()


# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     # try:
#     #     post = Post.objects.get(pk=pk)   #DoesNotExist 예외
#     # except Post.DoesNotExist:
#     #     raise Http404
    
#     return render(request, 'instagram/post_detail.html',{
#         'post':post,
#     })
    
post_detail = DetailView.as_view(
    model=Post,
    queryset=Post.objects.filter(is_public=True))

   
    
    

class PostDetailView(DetailView):
    model = Post
    # queryset = Post.objects.filter(is_public=True)
    def get_queryset(self):
        qs = super().get_queryset()
        
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        return qs

post_detail = PostDetailView.as_view()

def archives_year(request, year):
    return HttpResponse(f"{year}년 archives_year")