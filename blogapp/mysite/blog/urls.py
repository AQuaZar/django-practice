from django.conf.urls import url
from . import views

app_name = "blog"

urlpatterns = [
    url("", views.post_list, name="post_list"),
    url(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.post_detail,
        name="post_detail",
    ),
]
