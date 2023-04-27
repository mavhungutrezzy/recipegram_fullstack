from django import forms

from .models import MEAL_TYPE_CHOICES, TAGS_CHOICES, Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title",
            "description",
            "image",
            "ingredients",
            "instructions",
            "tags",
        ]

    image = forms.ImageField(required=False)
    ingredients = forms.CharField(widget=forms.Textarea)
    instructions = forms.CharField(widget=forms.Textarea)
    servings = forms.IntegerField(min_value=1)
    preparation_time = forms.IntegerField(min_value=0)
    cook_time = forms.IntegerField(min_value=0)
    total_time = forms.IntegerField(min_value=0)
    tags = forms.ChoiceField(choices=TAGS_CHOICES)
    meal_type = forms.ChoiceField(choices=MEAL_TYPE_CHOICES)
