from django.views.generic import ListView, DetailView
from posts.models import Post
# Create your views here.
class PostListView(ListView):
    model=Post

class PostDetail(DetailView):
    model = Post
    slug_field = "title"