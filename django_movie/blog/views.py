from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View
from .models import Post, Tag

from .utils import *
from .forms import TagForm, PostForm


def posts_list(reguest):
    posts = Post.objects.all()
    return render(reguest, "blog/index.html", context={"posts": posts})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = "blog/post_detail.html"


class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = "blog/post_create_form.html"



class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = "blog/tag_detail.html"


class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = "blog/tag_create.html"



def tags_list(reguest):
    tags = Tag.objects.all()
    return render(reguest, "blog/tags_list.html", context={"tags": tags})




