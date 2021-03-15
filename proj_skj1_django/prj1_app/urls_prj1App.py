#khlee add 21/02/17
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views #khlee add 21/03/01



urlpatterns = [
#    path('', views.prj1App_index, name='prj1App_index'),
    path('', views.prj1App_index.as_view(), name='prj1App_index'), #khlee modify 21/03/11
#    path('prj1App/', views.prj1App_index.as_view(), name='prj1App_index'),   #khlee modify 21/03/08
    
    
#    path('prj1App_category1/', views.prj1App_category1, name='prj1App_category1'),
#    path('prj1App_category2/', views.prj1App_category2, name='prj1App_category2'),
#    path('prj1App_testLink1/', views.prj1App_testLink1, name='prj1App_testLink1'),
#    path('prj1App_testLink2/', views.prj1App_testLink2, name='prj1App_testLink2'),
#    path('prj1App_about/', views.prj1App_about, name='prj1App_about'),
#    path('prj1App_userBlogNew/', views.prj1App_userBlogNew, name='prj1App_userBlogNew'),

    
    path('category1/', views.prj1App_category1, name='prj1App_category1'),
    path('category2/', views.prj1App_category2, name='prj1App_category2'),
    path('testLink1/', views.prj1App_testLink1, name='prj1App_testLink1'),
    path('testLink2/', views.prj1App_testLink2, name='prj1App_testLink2'),
    path('about/', views.prj1App_about, name='prj1App_about'),
#    path('userBlogNew/', views.prj1App_userBlogNew, name='prj1App_userBlogNew'),
#    path('BlogCreate/', views.prj1App_BlogCreate.as_view(), name='prj1App_blog_create'),
    path('BlogCreate/', views.prj1App_BlogCreate, name='prj1App_blog_create'),
    
    path('BlogDetail/<int:pk>', views.prj1App_BlogDetailView.as_view(), name='prj1App_blog-detail'), #khlee add 21/03/11
    path('BlogDetail/<int:pk>/comment/', views.prj1App_BlogCommentCreate.as_view(), name='prj1App_blog_comment'), #khlee add 21/03/11

]