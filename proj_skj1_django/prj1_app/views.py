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
from django.views import generic #khlee add 21/03/07
from .models import prj1_Blog, prj1_BlogComment #khlee mod 21/03/11

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
#def prj1App_index(request):
#    return render(request, "prj1_app/prj1App_index.html")

#khlee modify 21/03/08

class prj1App_index(generic.ListView):
    model = prj1_Blog
    paginate_by = 5
    template_name ='prj1_app/prj1App_index.html'



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

#def prj1App_userBlogNew(request):
#    return render(request, "prj1_app/prj1App_userBlogNew.html")



#khlee add 21/03/11
class prj1App_BlogDetailView(generic.DetailView):
    """
    Generic class-based detail view for a blog.
    """
    model = prj1_Blog
    
    


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse

from django.shortcuts import get_object_or_404


class prj1App_BlogCommentCreate(LoginRequiredMixin, CreateView):
    """
    Form for adding a blog comment. Requires login. 
    """
    model = prj1_BlogComment
    fields = ['description',]

    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(prj1App_BlogCommentCreate, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['prj1_blog'] = get_object_or_404(prj1_Blog, pk = self.kwargs['pk'])
        return context
        
    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.author = self.request.user
        #Associate comment with blog based on passed id
        form.instance.blog=get_object_or_404(prj1_Blog, pk = self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(prj1App_BlogCommentCreate, self).form_valid(form)

    def get_success_url(self): 
        """
        After posting comment return to associated blog.
        """
        return reverse('prj1App_blog_comment', kwargs={'pk': self.kwargs['pk'],})


from django.views.generic.edit import CreateView    
from django.contrib.auth.mixins import PermissionRequiredMixin

class prj1App_BlogCreate(CreateView):
    model = prj1_Blog
    fields = ['title', 'author', 'description']
