from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register("Post", views.IntruderImage)

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path("post/new", views.post_new, name="post_new"),
    path("api/", include(router.urls)),
]
