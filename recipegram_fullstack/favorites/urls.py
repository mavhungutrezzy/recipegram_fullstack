from django.urls import path

from . import views

app_name = "favorites"

urlpatterns = [
    path("list/", views.favorites_list, name="list"),
    path("add/<uuid:recipe_id>/", views.add_to_favorites, name="add"),
    path("remove/<uuid:recipe_id>/", views.remove_from_favorites, name="remove"),
]
