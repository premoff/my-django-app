from django.db import models
from django.urls import reverse
# Create your models here.
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Post(models.Model):
  title =  models.CharField(max_length=200, unique=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  #content = models.TextField()
  content = RichTextField()


  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('home')
  
