from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post

# Create your views here.

class blog(generic.ListView):
    """ A view to return the blog page """
    queryset = Post.objects.all()
    template_name = "blog/blog.html"
    paginate_by = 3

def post_detail(request, slug):
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request, "blog/post_detail.html",{"post": post,},
    )

class like_posts(generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse("post_detail", kwargs={"slug": self.kwargs.get("slug")})

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, slug=self.kwargs.get("slug"))

        if request.user in post.like.all():
            post.like.remove(request.user)
        else:
            post.like.add(request.user)

        return super().post(request, *args, **kwargs)
