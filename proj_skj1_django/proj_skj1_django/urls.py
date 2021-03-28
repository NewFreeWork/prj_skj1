"""proj_skj1_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#urlpatterns = [
#    path('admin/', admin.site.urls),
#]

#khlee add 21/02/01
from django.urls import include, path
from rest_framework import routers
from prj1_app import views, urls_prj1App
from django.conf import settings #khlee add 21/02/09
from django.conf.urls.static import static #khlee add 21/02/09
from django.contrib.auth import views as auth_views #khlee add 21/03/01
from django.conf.urls import url #khlee add 21/03/01


admin.site.site_header = 'Code Plane Admin' #khlee add 21/03/11


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'person', views.PersonViewSet)



#khlee add 21/03/06
urlpatterns = [
    path('admin/', admin.site.urls),
]



# Use include() to add URLS from the blog application 
from django.urls import include

urlpatterns += [
#    path('blog/', include('blog.urls')),
]


#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
urlpatterns += [
#    path('', RedirectView.as_view(url='/blog/', permanent=True)),
]



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

from django.views.generic import RedirectView

urlpatterns += [
    
#    path('', include(urls_prj1App)), #khlee add 21/02/17
    
#    path('prj1App_category1/', include(urls_prj1App)), #khlee add 21/02/26
#    path('prj1App_category2/', include(urls_prj1App)), #khlee add 21/02/26
#    path('prj1App_testLink1/', include(urls_prj1App)), #khlee add 21/02/26
#    path('prj1App_testLink2/', include(urls_prj1App)), #khlee add 21/02/26
#    path('prj1App_about/', include(urls_prj1App)), #khlee add 21/02/26
#    path('prj1App_userBlogNew/', include(urls_prj1App)), #khlee add 21/02/26

    
    
    
    #khlee add 21/03/01
    url(r'^accounts/', include('django.contrib.auth.urls')),
    
#    path('', include(router.urls)),
#    path('admin/', admin.site.urls),
    
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),


    
    path('prj1App/', include(urls_prj1App)), #khlee add 21/03/09
    path('summernote/', include('django_summernote.urls')), #khlee add 21/03/14
    url(r'^comments/', include('django_comments_xtd.urls')), #khlee add 21/03/28
    
    path('', RedirectView.as_view(url='/prj1App/', permanent=False)), #khlee add 21/03/09
#    path('', include(urls_prj1App)), #khlee add 21/03/11
        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

