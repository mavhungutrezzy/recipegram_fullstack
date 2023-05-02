# context_processors.py
from .models import Favorite


def favorites(request):
    if request.user.is_authenticated:
        favorites = Favorite.objects.filter(user=request.user).order_by("-created_at")
        favorites = [favorite.recipe for favorite in favorites]

    else:
        favorites = []

    return {"favorites": favorites}
