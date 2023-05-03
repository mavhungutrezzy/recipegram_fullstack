from .models import ShoppingList


def shopping_lists(request):
    # Add the shopping list to the context of every page.
    if request.user.is_authenticated:
        shopping_list = ShoppingList.objects.filter(user=request.user).order_by(
            "-created_at"
        )
        shopping_list = [item.recipe for item in shopping_list]
    else:
        shopping_list = []

    return {"shopping_list": shopping_list}
