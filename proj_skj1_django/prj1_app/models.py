from django.db import models

# Create your models here.
from django.contrib.auth.models import User #Blog author or commenter


#khlee add 21/02/09
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(default='media/default_image.jpeg')

    

#khlee add 21/03/03
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    
    
#khlee add 21/03/06
class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish.true)    

    
#khlee add 21/03/11    
from django.urls import reverse #Used to generate URLs by reversing the URL patterns    
    

class prj1_BlogAuthor(models.Model):
    
    #Model representing a blogger.
    
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=400, help_text="Enter your bio details here.")
    
    class Meta:
        ordering = ["user","bio"]

#    def get_absolute_url(self):
        
        #Returns the url to access a particular blog-author instance.
        
#        return reverse('blogs-by-author', args=[str(self.id)])

    def __str__(self):
        
        #String for representing the Model object.
        
        return self.user.username


class prj1_Blog(models.Model):
    
    #Model representing a blog post.
    
    title = models.CharField(max_length=200)
    author = models.ForeignKey(prj1_BlogAuthor, on_delete=models.SET_NULL, null=True)
      # Foreign Key used because Blog can only have one author/User, but bloggsers can have multiple blog posts.
    description = models.TextField(max_length=2000, help_text="Enter you blog text here.")
    
#    slug = models.SlugField(max_length=201, db_index=True, unique=True, allow_unicode=True)
    publish = models.BooleanField(default=True)
    
#    post_date = models.DateField(default=date.today)
    post_date = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    objects = EntryQuerySet.as_manager()
    
    
    class Meta:
        ordering = ["-post_date"]

    def get_absolute_url(self):
        #Returns the url to access a particular blog instance.
        return reverse('prj1App_blog-detail', args=[str(self.id)])

    def __str__(self):
        #String for representing the Model object.
        return self.title

    
#khlee add 21/03/11    
class prj1_BlogComment(models.Model):
    """
    Model representing a comment against a blog post.
    """
    description = models.TextField(max_length=1000, help_text="Enter comment about blog here.")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
      # Foreign Key used because BlogComment can only have one author/User, but users can have multiple comments
    post_date = models.DateTimeField(auto_now_add=True)
    blog= models.ForeignKey(prj1_Blog, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["post_date"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        len_title=75
        if len(self.description)>len_title:
            titlestring=self.description[:len_title] + '...'
        else:
            titlestring=self.description
        return titlestring    
    