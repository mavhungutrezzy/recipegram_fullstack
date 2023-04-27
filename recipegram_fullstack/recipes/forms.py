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

        labels = {
            "title": "Recipe Title",
            "description": "Description",
            "image": "Image",
            "ingredients": "Ingredients",
            "instructions": "Instructions",
            "tags": "Tags",
        }

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "ingredients": forms.Textarea(attrs={"class": "form-control"}),
            "instructions": forms.Textarea(attrs={"class": "form-control"}),
            "tags": forms.Select(attrs={"class": "form-control"}),
        }

    servings = forms.IntegerField(
        label="Servings",
        min_value=1,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )

    preparation_time = forms.IntegerField(
        label="Preparation Time (in minutes)",
        min_value=0,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )

    cook_time = forms.IntegerField(
        label="Cook Time (in minutes)",
        min_value=0,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )

    total_time = forms.IntegerField(
        label="Total Time (in minutes)",
        min_value=0,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )

    meal_type = forms.ChoiceField(
        label="Meal Type",
        choices=MEAL_TYPE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    tags = forms.ChoiceField(
        label="Tags",
        choices=TAGS_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
