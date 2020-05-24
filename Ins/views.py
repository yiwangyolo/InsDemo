from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post

# Create your views here.
class HomePage(TemplateView):
    template_name = 'home.html'

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    login_url = 'login'
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    template_name = 'make_post.html'

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title']
    template_name = 'edit_post.html'

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    template_name = 'delete_post.html'

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'sign_up.html'