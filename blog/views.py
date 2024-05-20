from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from .models import Post
from .forms import PostForm

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
        request, "blog/post_detail.html", {"post": post, },
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


@login_required
def add_post(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.slug = slugify(post.title)
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('blog'))
        else:
            messages.error(
                request,
                'Failed to add post. Please ensure the form is valid.'
            )
    else:
        form = PostForm()
    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
