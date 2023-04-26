import uuid

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

TAGS_CHOICES = (
    ("breakfast", "Breakfast"),
    ("lunch", "Lunch"),
    ("dinner", "Dinner"),
)


class Recipe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="recipes/", null=True, blank=True)
    ingredients = models.JSONField()
    instructions = models.JSONField()
    tags = models.CharField(max_length=255, choices=TAGS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title
