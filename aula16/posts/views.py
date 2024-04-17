from django.forms.forms import BaseForm
from django.shortcuts import render
from django.views.generic import ListView, FormView
from django.views.generic.detail import DetailView
from posts.forms import LoginForm
from posts.models import Post
from django.contrib.auth import authenticate
# Create your views here.

class PostView(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post
    slug_field = "title"

class LoginView(FormView):
    form_class=LoginForm
    success_url="/posts/"
    template_name="posts/login.html"
    def form_valid(self, form):
        username=form.cleaned_data['username']
        password=form.cleaned_data['password']
        
        return authenticate(username=username, password=password)
        
