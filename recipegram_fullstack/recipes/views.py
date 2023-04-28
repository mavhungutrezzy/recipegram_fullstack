from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from .forms import RecipeForm
from .models import Recipe

User = get_user_model()


@login_required
def index(request):
    recipes = Recipe.objects.all().order_by("-created_at")
    favorites = request.user.favorites.all()
    paginator = Paginator(recipes, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj, "favorites": favorites}
    return render(request, "recipes/index.html", context)


@login_required
def create(request):
    form = RecipeForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            form.save_m2m()
            return JsonResponse({"url": recipe.get_absolute_url()})
        return JsonResponse({"errors": form.errors}, status=400)
    return render(request, "recipes/create.html", {"form": form})


def detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, "recipes/detail.html", {"recipe": recipe})


@login_required
def edit(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    form = RecipeForm(request.POST, request.FILES, instance=recipe)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return JsonResponse({"url": recipe.get_absolute_url()})
        return JsonResponse({"errors": form.errors}, status=400)
    context = {"form": form}
    return render(request, "recipes/edit.html", context)


@login_required
@require_POST
def delete(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    recipe.delete()
    return JsonResponse({"deleted": True})
