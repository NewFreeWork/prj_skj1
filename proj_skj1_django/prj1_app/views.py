from django.shortcuts import render
from .models import Person

# Create your views here.

#khlee add start 21/01/30
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from prj1_app.serializers import UserSerializer, GroupSerializer
from .models import Person #khlee add 21/02/09
from .serializers import PersonSerializer #khlee add 21/02/09


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



#khlee add end
