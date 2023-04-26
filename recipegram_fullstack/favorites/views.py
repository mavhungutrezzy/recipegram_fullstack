from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from .models import Favorite
from recipes.models import Recipe

User = get_user_model()


def index(request):
    favorites = Favorite.objects.all().order_by("-created_at")
    paginator = Paginator(favorites, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "favorites/index.html", {"page_obj": page_obj})

