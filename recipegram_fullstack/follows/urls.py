from django.urls import path

from . import views

app_name = "follows"

urlpatterns = [
    path("follow/<str:username>/", views.follow, name="follow"),
    path("unfollow/<str:username>/", views.unfollow, name="unfollow"),
    path("followers/", views.followers, name="followers"),
    path("following/", views.following, name="following"),
    path("recipes/<str:username>/", views.user_recipes, name="user_recipes"),
]
