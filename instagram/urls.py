from django.urls import path, re_path , register_converter
from . import views



# 커스텀 컨버터
class YearConverter:
    regex = r"20\d{2}"
    
    def to_python(self, value):
        return int(value)
    
    def to_url(self, value):
        return str(value)




register_converter(YearConverter, 'year')



app_name = 'instagram' # URL Reverse 에서 namespace 역할을 하게됨

urlpatterns = [
    path('',views.post_list),
    path('<int:pk>', views.post_detail),
    # re_path(r'(?P<pk>\d+)/$', views.post_detial),
    # path('archives/<int:year>/', views.archives_year),
    # re_path(r'archives/(?P<year>\d+)/', views.archives_year),
    # re_path(r'archives/(?P<year>\d{4})/', views.archives_year),
    # re_path(r'archives/(?P<year>20\d{2})/', views.archives_year),
    path('archives/<year:year>/', views.archives_year),
    
    
]
