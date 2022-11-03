from django.urls import path
from .views import *

app_name ="blog" #url 'blog:list'


urlpatterns = [
    path('', post_list, name='list'),
    path('create/', post_create, name='create'),
    path('<str:slug>/', post_detail, name='detail'),
    path('<str:slug>/update/', post_update, name='update'),
    path('<str:slug>/delete/', post_delete, name='delete'),
    path('<str:slug>/like/', post_like, name='like'),
]
