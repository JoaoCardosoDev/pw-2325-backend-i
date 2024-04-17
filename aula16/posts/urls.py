
from django.urls import path
from django.contrib.auth.decorators import login_required
from posts.views import PostDetail, PostView, LoginView


urlpatterns = [
    path("", login_required(PostView.as_view()), name="post_list"),
    path("<slug>", PostDetail.as_view(), name="post_detail"),
    path("login/", LoginView.as_view())
]