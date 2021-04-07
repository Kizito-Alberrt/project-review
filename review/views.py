from review.models import Post
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import form
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.template import context
# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

def likeview(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('review', args=[str(pk)]))


class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date']

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