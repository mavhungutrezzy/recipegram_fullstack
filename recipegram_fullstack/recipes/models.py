import uuid

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

MEAL_TYPE_CHOICES = (
    ("breakfast", "Breakfast"),
    ("lunch", "Lunch"),
    ("dinner", "Dinner"),
    ("snack", "Snack"),
    ("dessert", "Dessert"),
    ("beverage", "Beverage"),
    ("other", "Other"),
)

TAGS_CHOICES = (
    ("vegan", "Vegan"),
    ("vegetarian", "Vegetarian"),
    ("gluten-free", "Gluten Free"),
    ("dairy-free", "Dairy Free"),
    ("Indian", "Indian"),
    ("Italian", "Italian"),
    ("Mexican", "Mexican"),
    ("Chinese", "Chinese"),
    ("Japanese", "Japanese"),
    ("Thai", "Thai"),
    ("Korean", "Korean"),
)


class Recipe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="recipes/", null=True, blank=True)
    ingredients = models.JSONField()
    instructions = models.JSONField()
    servings = models.PositiveIntegerField(default=1)
    meal_type = models.CharField(max_length=255, choices=MEAL_TYPE_CHOICES)
    tags = models.CharField(max_length=255, choices=TAGS_CHOICES)
    preparation_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    total_time = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title
