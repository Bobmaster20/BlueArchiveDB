from django.urls import path
from . import views

# URL Patterns
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:char_name>",views.character, name="character")
]