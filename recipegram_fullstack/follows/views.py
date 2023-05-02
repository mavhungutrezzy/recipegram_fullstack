from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from recipes.models import Recipe

from .models import Follow

User = get_user_model()


@login_required
def follow(request, username):
    user = get_object_or_404(User, username=username)
    follow, created = Follow.objects.get_or_create(
        follower=request.user, following=user
    )
    if created:
        message = f"You are now following {user.username}"
    else:
        message = f"You are already following {user.username}"
    data = {"message": message}
    return JsonResponse(data)


@login_required
def unfollow(request, username):
    user = get_object_or_404(User, username=username)
    Follow.objects.filter(follower=request.user, following=user).delete()
    message = f"You are no longer following {user.username}"
    data = {"message": message}
    return JsonResponse(data)


@login_required
def followers(request):
    followers = Follow.objects.filter(following=request.user).order_by("-created_at")
    paginator = Paginator(followers, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "follows/followers.html", {"page_obj": page_obj})


@login_required
def following(request):
    following = Follow.objects.filter(follower=request.user).order_by("-created_at")
    paginator = Paginator(following, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "follows/following.html", {"page_obj": page_obj})


@login_required
def user_recipes(request, username):
    user = get_object_or_404(User, username=username)
    recipes = Recipe.objects.filter(author=user).order_by("-created_at")
    paginator = Paginator(recipes, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request, "follows/user_recipes.html", {"user": user, "page_obj": page_obj}
    )
