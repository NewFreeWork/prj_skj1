from django.contrib import admin

# Register your models here.
from .models import prj1_BlogAuthor, prj1_Blog, prj1_BlogComment
from django_summernote.admin import SummernoteModelAdmin #khlee add 21/03/14


# Minimal registration of Models.
admin.site.register(prj1_BlogAuthor)
admin.site.register(prj1_BlogComment)


class BlogCommentsInline(admin.TabularInline):
    """
    Used to show 'existing' blog comments inline below associated blogs
    """
    model = prj1_BlogComment
    max_num=0


    


#@admin.register(prj1_Blog)
#class prj1_BlogAdmin(admin.ModelAdmin):
class prj1_BlogAdmin(SummernoteModelAdmin):
    """
    Administration object for Blog models. 
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields), grouping the date fields horizontally
     - adds inline addition of blog comments in blog view (inlines)
    """
    summernote_fields = '__all__'
    
    list_display = ('title', 'author', 'post_date')
    inlines = [BlogCommentsInline]
    
admin.site.register(prj1_Blog, prj1_BlogAdmin) #khlee add 21/03/14


#khlee add 21/03/17
from .models import File, Message

# Minimal registration of Models.
admin.site.register(File)
admin.site.register(Message)

