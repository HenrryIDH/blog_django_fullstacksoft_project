from email.policy import default
from random import choices
from django.db import models
from django.contrib.auth.models import User

# Register your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


def user_dir_path(instance, filename):
    return f"user/{instance.author.id}/{filename}"


class Post(models.Model):

    OPTIONS = (
        ('d', 'Draft'),
        ('p', 'Published')
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, blank=True, null=True)

    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to=user_dir_path, default="default.png")
    publish_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True)
    status = models.CharField(max_length=1, choices=OPTIONS, default='d')

    def __str__(self):
        return self.title

    def comment_count(self):
        return self.comment_set.all().count()

    def view_count(self):
        return self.postview_set.all().count()

    def like_count(self):
        return self.like_set.all().count()

    def comments(self):
        return self.comment_set.all()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    time_stamp = models.DateTimeField(auto_now_add=True)
    content= models.TextField()

    def __str__(self):
        return self.user.username

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username



