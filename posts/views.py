"""Posts views."""

# Django
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView

# Forms
from posts.forms import PostForm, MausoleoForm

# Models
from posts.models import Post, Mausoleo

class CreateMausoleoView(CreateView):
    """Create a new post."""

    template_name = 'posts/createmausoleo.html'
    form_class = MausoleoForm
    success_url = reverse_lazy('posts:feed')


class PostsFeedView(ListView):
    """Return all published posts."""

    template_name = 'posts/feed.html'
    model = Mausoleo
    context_object_name = 'posts'

class QRView(DetailView):
    """Return all published posts."""

    template_name = 'posts/qr.html'
    queryset = Mausoleo.objects.all()
    context_object_name = 'maus'


class PostDetailView(DetailView):
    """Return post detail."""

    template_name = 'posts/index.html'
    queryset = Mausoleo.objects.all()
    context_object_name = 'maus'


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post."""

    template_name = 'posts/createmausoleo.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context
