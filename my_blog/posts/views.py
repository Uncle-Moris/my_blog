from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post
from tags.models import Tag


def posts_list(request):
    posts_list = Post.objects.all()
    tags_list = Tag.objects.all()
    q = request.GET.get("title")
    tag = request.GET.get("tags")
    if q:
        posts_list = posts_list.filter(title__icontains=q)
    context = {'posts_list': posts_list, 'tags_list': tags_list}
    return render(request,'posts/list.html', context)


def posts_details(request, post_id: int):
    post_details = Post.objects.get(pk=post_id)
    context = {'details': post_details}
    return render(request, 'posts/details.html', context)

