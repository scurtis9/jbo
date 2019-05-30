from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import (
    View,
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import CommentForm
from .models import Post, Category, Comment


class PostListView(ListView):
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def get_queryset(self):
        return Post.objects.all()


class PostDisplay(DetailView):
    template_name = 'blog/post_detail.html'
    model = Post

    def get_object(self):
        obj = super().get_object()
        obj.save()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            context['form'] = CommentForm(initial={'post': self.object, 'author': self.request.user.get_full_name()})

        context['comments'] = Comment.objects.filter(post=self.object)
        return context


class PostComment(SingleObjectMixin, FormView):
    template_name = 'blog/post_detail.html'
    form_class = CommentForm
    model = Post

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail', kwargs={'pk': self.object.pk})


class PostDetailView(View):

    def get(self, request, *args, **kwargs):
        view = PostDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostComment.as_view()
        return view(request, *args, **kwargs)


class PostCategoryListView(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'posts'

    def get_queryset(self):
        self.category = get_object_or_404(Category, name=self.kwargs['category'])
        return Post.objects.filter(categories=self.category)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
