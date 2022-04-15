from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView, MonthArchiveView, \
    WeekArchiveView, DayArchiveView, TodayArchiveView, DateDetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView, MonthArchiveView, \
    WeekArchiveView, DayArchiveView, TodayArchiveView, DateDetailView

from .forms import PostForm
from .models import Post
from django.contrib import messages


# @login_required
# def post_new(request):
#     # models.GenericIPAddressField   ip주소 저장가능
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user  # 현재 로그인 유저 Instance
#             post.save()
#             messages.success(request, '포스팅을 저장했습니다.')
#             return redirect(post)
#     else:
#         form = PostForm()
#
#     return render(request, 'instagram/post_form.html', {
#         'form': form,
#         'post': None,
#     })

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        messages.success(self.request, '포스팅을 저장했습니다.')
        return super().form_valid(form)


post_new = PostCreateView.as_view()


# @login_required
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     # 작성자 체크 tip 추후 장식자 로 만들어서 활용가능
#     if post.author != request.user:
#         messages.error(request, '작성자만 수정 할 수 있습니다. ')
#         return redirect(post)
#
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             post = form.save()
#             messages.success(request, '포스팅을 수정했습니다.')
#
#             return redirect(post)
#     else:
#         form = PostForm(instance=post)
#
#     return render(request, 'instagram/post_form.html', {
#         'form': form,
#         'post': post,
#     })


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        messages.success(self.request, '포스팅을 수정했습니다.')
        return super().form_valid(form)


post_edit = PostUpdateView.as_view()


#
# @login_required
# def post_delete(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         messages.success(request, '포스팅을 삭제했습니다.')
#         return redirect('instagram:post_list')
#     return render(request, 'instagram/post_confirm_delete.html', {
#         'post': post,
#     })

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('instagram:post_list')
    # def get_success_url(self):
    #     return reverse('instagram:post_list')


post_delete = PostDeleteView.as_view()


# @login_required
# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q','')
#     if q:
#         qs = qs.filter(message__icontains=q)


#     messages.info(request,'messages 테스트')


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

post_archive_year = YearArchiveView.as_view(model=Post, date_field='created_at', make_object_list=True)

post_archive_month = MonthArchiveView.as_view(model=Post, date_field='created_at', month_format='%m')

post_archive_week = WeekArchiveView.as_view(model=Post, date_field='created_at',
                                            week_format='%U')  # 한주시작 일요일 -> %U 월요일 -> %W

post_archive_day = DayArchiveView.as_view(model=Post, date_field='created_at', month_format='%m')

post_archive_today = TodayArchiveView.as_view(model=Post, date_field='created_at')

post_archive_datedetial = DateDetailView.as_view(model=Post, date_field='created_at', month_format='%m')
