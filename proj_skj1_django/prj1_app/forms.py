from django import forms


#khlee add 21/03/03
class LoginForm(forms.Form):
    # LoginForm 에서 입력받을 값은 2개 (아이디, 패스워드)
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    
    
    

from .models import prj1_BlogAuthor, prj1_Blog
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


#class CreateBlogForm(forms.Form):
class  CreateBlogForm(forms.ModelForm):
    #title = forms.CharField(max_length=200)
    #author = forms.ModelChoiceField(queryset=prj1_BlogAuthor.objects.all())
      # Foreign Key used because Blog can only have one author/User, but bloggsers can have multiple blog posts.
    #description = forms.CharField(widget=forms.Textarea)
    
        #model = prj1_Blog
        #fields = ['title', 'author', 'description']
        
    #description = forms.CharField(widget=SummernoteWidget()) # iframe으로 적용
    #description = forms.CharField(widget=SummernoteInplaceWidget())
    
    #widgets = {
        #'description': SummernoteWidget(),
    #}
    class Meta:
        model = prj1_Blog
        fields = ['title', 'author', 'description']
        widgets = {
            'description': SummernoteWidget(),
        }

    
    
"""        
class FormFromSModel(forms.ModelForm):
    class Meta:
        model = prj1_Blog
        
        widgets = {
            'description': SummernoteWidget(),
        }
"""            