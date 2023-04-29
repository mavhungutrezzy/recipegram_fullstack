import uuid

from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
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
    image = models.ImageField(upload_to="recipes")
    author = models.ForeignKey(User, related_name="recipes", on_delete=models.CASCADE)
    tags = ArrayField(
        models.CharField(max_length=255, choices=TAGS_CHOICES), blank=True
    )
    meal_type = ArrayField(
        models.CharField(max_length=255, choices=MEAL_TYPE_CHOICES), blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ingredients = ArrayField(models.CharField(max_length=255), blank=True)
    instructions = ArrayField(models.CharField(max_length=255), blank=True)
    servings = models.PositiveIntegerField()
    prep_time_in_minutes = models.PositiveIntegerField()
    cook_time_in_minutes = models.PositiveIntegerField()
    total_time = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} by {self.author.username}"

    def get_absolute_url(self):
        return f"/recipes/{self.id}/"
