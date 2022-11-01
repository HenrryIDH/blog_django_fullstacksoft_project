from django.shortcuts import render, redirect, get_object_or_404

from .models import Post, Like, PostView, Comment
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from django.contrib import messages
import uuid
from django.template.defaultfilters import slugify

# Create your views here.


def get_random_code():
    code = str(uuid.uuid4())[:11].replace("-", "")
    return code


def post_list(request):
    data = Post.objects.filter(status='p')
    context = {
        'object_list': data
    }
    return render(request, "blog/post_list.html", context)
