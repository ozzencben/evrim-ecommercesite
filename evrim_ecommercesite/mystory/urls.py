from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_story, name="my_story"),
]