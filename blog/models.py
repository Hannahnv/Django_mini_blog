from django.db import models

# Create your models here.

from datetime import date
from django.urls import reverse 
from django.contrib.auth.models import User 
from django.utils import timezone


'''
Each comment will have only one blog, but a blog may have many comments.
Blog posts and comments must be sorted by post date.
Not every user will necessarily be a blog author though any user may be a commenter.
Blog authors must also include bio information.'''


# Model representing a blog author

class BlogAuthor(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=400, help_text='Enter your bio details here.')
    
    class Meta:
        ordering = ["user", "bio"]
        
    def get_absolute_url(self):
        return reverse('blogs-by-author', args=[str(self.id)])
    
    def __str__(self):
        return self.user.username
    
    
# Model representing a blog post

class Blog(models.Model):    
    name = models.CharField(max_length=200)
    # Blog only have 1 author/user, but bloggers have mutiple blog posts
    author = models.ForeignKey(BlogAuthor, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=2000, help_text = "Enter your blog text here.")
    post_date = models.DateField(default=timezone.now)
    
    class Meta:
        ordering = ["-post_date"]
    def get_absolute_url(self):
        return reverse("blog-detail", args=[str(self.id)])
    def __str__(self):
        return self.name
    
    

class BlogComment(models.Model):
    description = models.TextField(max_length=1000, help_text="Enter comment about blog here.")
    # Blog Comment only have 1 author/user, but users have mutiple comments
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_date=models.DateTimeField(auto_now_add=True)
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE) #A foreign key linking to Blog. If the blog is deleted, the comment is also deleted.
    
    class Meta:
        ordering = ["post_date"]

    def __str__(self):
        '''Returns a truncated version of the comment description for display, up to 75 characters.'''
        len_title=75
        if len(self.description)>len_title:
            titlestring=self.description[:len_title] + '...'
        else:
            titlestring=self.description
        return titlestring