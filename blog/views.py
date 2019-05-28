from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.views import generic

from .forms import CommentForm
from .models import Post, Category, Comment


class PostListView(generic.ListView):
    template_name = 'blog/posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()


class PostDetailView(generic.edit.FormMixin, generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('blog:detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={
            'post': self.object
        })
        context['comments'] = Comment.objects.filter(post=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(PostDetailView, self).form_valid(form)


class PostCategoryListView(generic.ListView):
    template_name = 'blog/category.html'
    context_object_name = 'posts'

    def get_queryset(self):
        self.category = get_object_or_404(Category, name=self.kwargs['category'])
        return Post.objects.filter(categories=self.category)
