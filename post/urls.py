from django.urls import path, re_path
from post.views import (
    CreatePostAPIView,
    ListPostAPIView,
    DetailPostAPIView,
    CreateCommentAPIView,
    ListCommentAPIView,
    DetailCommentAPIView,
    PostDetailApiView,
    ListAllPostAPIView,
)

app_name = "posts"

urlpatterns = [
    path("", ListPostAPIView.as_view(), name="list_post"),
    path("allpost/", ListAllPostAPIView.as_view(), name="list_post"),
    path("create/", CreatePostAPIView.as_view(), name="create_post"),
    path('search/', ListAllPostAPIView.as_view(), name='postsearch'),
    path("<str:slug>/", DetailPostAPIView.as_view(), name="post_detail"),
    path("edit/<str:slug>/", DetailPostAPIView.as_view(), name="post_edit"),
    path("<str:slug>/comment/", ListCommentAPIView.as_view(), name="list_comment"),
    path(
        "<str:slug>/comment/create/",
        CreateCommentAPIView.as_view(),
        name="create_comment",
    ),
    path(
        "<str:slug>/comment/<int:id>/",
        DetailCommentAPIView.as_view(),
        name="comment_detail",
    ),
    re_path(r'(?P<slug>[\w-]+)/noteid/$', PostDetailApiView.as_view(), name='noteid'),
]