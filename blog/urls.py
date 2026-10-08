from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView, RegisterView, MyPostsView, about, contact
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("posts/new/", PostCreateView.as_view(), name="post_create"),
    path("posts/<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
    path("posts/<slug:slug>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("posts/<slug:slug>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("category/<slug:slug>/", PostListView.as_view(), name="category_posts"),
    path("my-posts/", MyPostsView.as_view(), name="my_posts"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
]