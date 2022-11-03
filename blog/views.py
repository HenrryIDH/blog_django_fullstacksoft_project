from django.shortcuts import render, redirect, get_object_or_404

from .models import Post, Like, PostView, Comment
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from django.contrib import messages
import uuid
from django.template.defaultfilters import slugify
# Create your views here.

def get_random_code():
    code = str(uuid.uuid4())[:11].replace("-","")
    return code

def post_list(request):
    data = Post.objects.filter(status='p')
    context = {
        'object_list' : data
    }

    return render(request, "blog/post_list.html", context)

@login_required()
def post_create(request):
    form = PostForm(request.POST or None, files=request.FILES)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.slug = slugify(post.title+" "+ get_random_code())
        post.save()
        messages.success(request, 'Post saved!')
        return redirect('blog:list')
    
    return render(request, 'blog/post_create.html', {'form':form})

def post_detail(request, slug):
    form = CommentForm()
    # data = Post.objects.get(slug=slug)
    data = get_object_or_404(Post, slug=slug)

    if request.user.is_authenticated:
        PostView.objects.get_or_create(user= request.user, post=data)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = data
            comment.save()
            return redirect("blog:detail", slug=slug)
    
    context = {
        "object": data,
        "form": form
    }

    return render(request, "blog/post_detail.html", context)

@login_required()
def post_update(request, slug):
    data = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=data)

    if request.user.id != data.author.id:
        messages.warning(request, "You are not owner of this post")
        return redirect("blog:list")

    if form.is_valid():
        form.save()
        messages.success(request, "Post Updated!")
        return redirect(request.path)

    context = {
        "object": data,
        "form": form
    }

    return render(request, "blog/post_update.html", context)

@login_required()
def post_delete(request, slug):
    data = get_object_or_404(Post, slug=slug)

    if request.user.id != data.author.id:
        messages.warning(request, "You are not owner of this post")
        return redirect("blog:list")

    if request.method == 'POST':
        data.delete()
        messages.success(request, "Post Deleted!")
        return redirect("blog:list")
    
    context = {
        "object":data
    }

    return render(request,"blog/post_delete.html", context)

@login_required()
def post_like(request, slug):
    if request.method == 'POST':
        data = get_object_or_404(Post, slug=slug)
        like_qs = Like.objects.filter(user=request.user, post=data)
        if like_qs.exists():
            like_qs[0].delete()
        else:
            Like.objects.create(user=request.user, post=data)

        return redirect("blog:detail", slug=slug)