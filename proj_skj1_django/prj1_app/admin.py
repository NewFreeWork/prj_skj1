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
    
    list_display = ('title', 'author', 'post_date', 'tag_list') #khlee mod 21/03/21
    inlines = [BlogCommentsInline]
    
    def get_queryset(self, request): #khlee add 21/03/21
        return super().get_queryset(request).prefetch_related('tags')
    def tag_list(self, obj): #khlee add 21/03/21
        return ','.join(o.name for o in obj.tags.all())
    
    
admin.site.register(prj1_Blog, prj1_BlogAdmin) #khlee add 21/03/14


#khlee add 21/03/17
from .models import File, Message


# Minimal registration of Models.
admin.site.register(File)
admin.site.register(Message)

