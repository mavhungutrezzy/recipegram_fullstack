from django.urls import path

from . import views

app_name = "recipes"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<uuid:recipe_id>/", views.detail, name="detail"),
    path("<uuid:recipe_id>/edit/", views.edit, name="edit"),
    path("<uuid:recipe_id>/delete/", views.delete, name="delete"),
]
