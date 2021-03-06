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
    path('BlogCreate/', views.prj1App_BlogCreate.as_view(), name='prj1App_blog_create'),
    
    path('BlogDetail/<int:pk>', views.prj1App_BlogDetailView.as_view(), name='prj1App_blog-detail'), #khlee add 21/03/11
    path('BlogDetail/<int:pk>/comment/', views.prj1App_BlogCommentCreate.as_view(), name='prj1App_blog_comment'), #khlee add 21/03/11

    path('downloadList/', views.prj1App_downloadList.as_view(), name='prj1App_downloadList'), #khlee add 21/03/17
    path('downloadList/<int:pk>', views.prj1App_downloadListDetail.as_view(), name='prj1App_downloadDetail'), #khlee add 21/03/28
    path('download/<int:id>/', views.download, name='prj1App_download'), #khlee add 21/03/17
    
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'), #khlee add 21/03/21
    path('tag/<str:tag>', views.TaggedObjectLV.as_view(), name='tagged_object_list'), #khlee add 21/03/21
    
    path('browser/searchData/', views.searchData, name='searchData'), #khlee add 21/03/25
]