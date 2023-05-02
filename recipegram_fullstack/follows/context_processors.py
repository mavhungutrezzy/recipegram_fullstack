# context_processors.py

from .models import Follow


def following(request):
    if request.user.is_authenticated:
        following = Follow.objects.filter(follower=request.user).order_by("-created_at")
        following = [follow.following for follow in following]

    else:
        following = []

    return {"following": following}
