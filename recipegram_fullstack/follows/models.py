import uuid

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Follow(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    follower = models.ForeignKey(
        User, related_name="following_set", on_delete=models.CASCADE
    )
    following = models.ForeignKey(
        User, related_name="follower_set", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("follower", "following")

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"
