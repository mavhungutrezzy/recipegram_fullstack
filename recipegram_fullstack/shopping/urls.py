from django.urls import path

from . import views

app_name = "shopping"

urlpatterns = [
    path("list/", views.shopping_list, name="list"),
    path("add/<uuid:recipe_id>/", views.add_to_shopping_list, name="add"),
    path("remove/<uuid:recipe_id>/", views.remove_from_shopping_list, name="remove"),
    path("download/", views.download_shopping_list, name="download"),
]
