import csv

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from recipes.models import Recipe

from .models import ShoppingList


@login_required
def add_to_shopping_list(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    created = ShoppingList.objects.get_or_create(user=request.user, recipe=recipe)
    if created:
        message = "Recipe added to shopping list!"
    else:
        message = "Recipe already in shopping list."
    data = {"message": message}
    return JsonResponse(data)


@login_required
def remove_from_shopping_list(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    ShoppingList.objects.filter(user=request.user, recipe=recipe).delete()
    message = "Recipe removed from shopping list!"
    data = {"message": message}
    return JsonResponse(data)


@login_required
def shopping_list(request):
    shopping_list = ShoppingList.objects.all().order_by("-created_at")
    paginator = Paginator(shopping_list, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "shopping/index.html", {"page_obj": page_obj})


@login_required
def download_shopping_list(request):
    user = request.user
    shopping_list = ShoppingList.objects.filter(user=user)
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="shopping_list.csv"'
    writer = csv.writer(response)
    writer.writerow(["title", "description", "ingredients"])
    for item in shopping_list:
        writer.writerow(
            [
                item.recipe.title,
                item.recipe.description,
                item.recipe.ingredients,
            ]
        )

    return response
