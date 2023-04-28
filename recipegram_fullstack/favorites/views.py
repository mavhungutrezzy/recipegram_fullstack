from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from recipes.models import Recipe

from .models import Favorite

User = get_user_model()


def favorites_list(request):
    favorites = Favorite.objects.all().order_by("-created_at")
    paginator = Paginator(favorites, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "favorites/index.html", {"page_obj": page_obj})


@login_required
def add_to_favorites(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    created = Favorite.objects.get_or_create(user=request.user, recipe=recipe)
    if created:
        message = "Recipe added to favorites!"
    else:
        message = "Recipe already in favorites."
    data = {"message": message}
    return JsonResponse(data)


@login_required
def remove_from_favorites(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    Favorite.objects.filter(user=request.user, recipe=recipe).delete()
    message = "Recipe removed from favorites!"
    data = {"message": message}
    return JsonResponse(data)
