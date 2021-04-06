from review.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

class Home(ListView):
    model = Post
    template_name = 'home.html'

class review(DetailView):
    model = Post
    template_name = 'review.html'