from django.http import Http404, HttpRequest, HttpResponse
from django.views.generic import ListView,DetailView,ArchiveIndexView,YearArchiveView,MonthArchiveView,WeekArchiveView,DayArchiveView,TodayArchiveView,DateDetailView
from django.shortcuts import redirect, render,get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import PostForm



def post_new(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = PostForm()
    
    
    return render(request, 'instagram/post_form.html',{
        'form':form,
    })










# @login_required
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



# post_list = login_required(ListView.as_view(model=Post, paginate_by=10))

@method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    model = Post
    paginate_by = 100

post_list = PostListView.as_view()



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
    
# post_detail = DetailView.as_view(
#     model=Post,
#     queryset=Post.objects.filter(is_public=True))

   
    
    

class PostDetailView(DetailView):
    model = Post
    # queryset = Post.objects.filter(is_public=True)
    def get_queryset(self):
        qs = super().get_queryset()
        
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        return qs

post_detail = PostDetailView.as_view()





# def archives_year(request, year):
#     return HttpResponse(f"{year}년 archives_year")



post_archive = ArchiveIndexView.as_view(model=Post, date_field='created_at', paginate_by=10)



post_archive_year = YearArchiveView.as_view(model=Post, date_field='created_at' , make_object_list=True)

post_archive_month = MonthArchiveView.as_view(model=Post, date_field='created_at',month_format='%m')

post_archive_week = WeekArchiveView.as_view(model=Post, date_field='created_at', week_format = '%U')   #한주시작 일요일 -> %U 월요일 -> %W

post_archive_day = DayArchiveView.as_view(model=Post, date_field='created_at',month_format='%m')

post_archive_today = TodayArchiveView.as_view(model=Post, date_field='created_at')

post_archive_datedetial = DateDetailView.as_view(model=Post, date_field='created_at', month_format = '%m')