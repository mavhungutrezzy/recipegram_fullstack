from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from recipes.models import Recipe

User = get_user_model()


class ShoppingList(models.Model):
    user = models.ForeignKey(
        User, related_name="shopping_lists", on_delete=models.CASCADE
    )
    recipe = models.ForeignKey(
        Recipe, related_name="shopping_lists", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Shopping List")
        verbose_name_plural = _("Shopping Lists")
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.user} - {self.recipe}"
