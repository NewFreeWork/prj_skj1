from django.contrib import admin

# Register your models here.


from .models import prj1_BlogAuthor, prj1_Blog, prj1_BlogComment


# Minimal registration of Models.
admin.site.register(prj1_BlogAuthor)
admin.site.register(prj1_BlogComment)


class BlogCommentsInline(admin.TabularInline):
    """
    Used to show 'existing' blog comments inline below associated blogs
    """
    model = prj1_BlogComment
    max_num=0


@admin.register(prj1_Blog)
class prj1_BlogAdmin(admin.ModelAdmin):
    """
    Administration object for Blog models. 
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields), grouping the date fields horizontally
     - adds inline addition of blog comments in blog view (inlines)
    """
    list_display = ('title', 'author', 'post_date')
    inlines = [BlogCommentsInline]
    