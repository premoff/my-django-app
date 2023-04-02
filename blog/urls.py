from django.urls import path
from .views import HomePage,DetailPage #,Addpost,UpdatePost,DeletePost

urlpatterns = [
    path('',HomePage.as_view(),name='home'),
    path('post/<int:pk>',DetailPage.as_view(),name='detail'),
   
]