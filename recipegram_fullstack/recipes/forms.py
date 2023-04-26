from django import forms

from .models import TAGS_CHOICES, Recipe


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
    tags = forms.ChoiceField(choices=TAGS_CHOICES)
