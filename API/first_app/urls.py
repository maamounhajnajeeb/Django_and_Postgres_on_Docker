from django.urls import path

from . import views

app_name = "first_app"


urlpatterns = [
    path("hello_world/", views.hello, name="hello_function"),
    path("add/name/", views.add_name, name="add_name"),
    path("all/names/", views.all_names, name="all_names"),
]
