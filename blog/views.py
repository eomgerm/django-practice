from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from rest_framework import viewsets

from blog.forms import PostForm

from .models import Post
from .serializers import PostSerializer

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        "published_date"
    )
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})


def post_new(reqeust):
    if reqeust.method == "POST":
        form = PostForm(reqeust.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = reqeust.user
            post.published_date = timezone.now()
            post.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(reqeust, "blog/post_edit.html", {"form": form})


class IntruderImage(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
