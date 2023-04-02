from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic import ListView,DetailView #CreateView,UpdateView,DeleteView
from .models import Post
#from .forms import Addpostform   #dealing posts help of forms
#from django.urls import reverse_lazy


class HomePage(ListView):
  model = Post
  template_name = 'blog/home.html'

class DetailPage(DetailView):
  model = Post
  template_name = 'blog/detail.html'

