from django.urls import path
from .views import *

app_name ="blog" #url 'blog:list'

urlpatterns = [
    path('', post_list, name='list')
]