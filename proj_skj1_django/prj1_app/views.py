from django.shortcuts import render
from .models import Person

# Create your views here.

#khlee add start 21/01/30
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from prj1_app.serializers import UserSerializer, GroupSerializer
#from .models import Person #khlee add 21/02/09
from .serializers import PersonSerializer #khlee add 21/02/09
#from . import urls_prj1App #khlee add 21/02/17


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer    

    
#khlee add 21/02/17
def prj1App_index(request):
    return render(request, "prj1_app/prj1App_index.html")


#khlee add 21/02/26
def prj1App_category1(request):
    return render(request, "prj1_app/prj1App_category1.html")

def prj1App_category2(request):
    return render(request, "prj1_app/prj1App_category2.html")

def prj1App_testLink1(request):
    return render(request, "prj1_app/prj1App_testLink1.html")

def prj1App_testLink2(request):
    return render(request, "prj1_app/prj1App_testLink2.html")

def prj1App_about(request):
    return render(request, "prj1_app/prj1App_about.html")

def prj1App_userBlogNew(request):
    return render(request, "prj1_app/prj1App_userBlogNew.html")


