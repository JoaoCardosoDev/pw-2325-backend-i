

from django.urls import path
from django.contrib.auth.decorators import login_required
from posts.views import PostListView, PostDetail


urlpatterns = [
    path("", login_required(PostListView.as_view()), name='posts'),
    path("<slug>", login_required(PostDetail.as_view()), name="post_detail")
]
