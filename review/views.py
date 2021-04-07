from review.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import form
from django.urls import reverse_lazy
# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

class review(DetailView):
    model = Post
    template_name = 'review.html'

class AddPostView(CreateView):
    model = Post
    form_class = form
    template_name = 'add_post.html'
    # fields = '__all__'

class update(UpdateView):
    model = Post
    form_class = form
    template_name = 'update_post.html'
    # fields = [ 'title', 'title_tag', 'body']

class delete(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')