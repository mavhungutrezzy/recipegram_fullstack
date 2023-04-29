from django import forms

from .models import MEAL_TYPE_CHOICES, TAGS_CHOICES, Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title",
            "description",
            "image",
            "tags",
            "meal_type",
            "ingredients",
            "instructions",
            "servings",
            "prep_time_in_minutes",
            "cook_time_in_minutes",
            "total_time",
        ]

    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control"})
    )
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"class": "form-control"})
    )
    tags = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=TAGS_CHOICES
    )
    meal_type = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=MEAL_TYPE_CHOICES
    )
    ingredients = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    instructions = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    servings = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    prep_time_in_minutes = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    cook_time_in_minutes = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    total_time = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    def clean_ingredients(self):
        if ingredients := self.cleaned_data.get("ingredients"):
            return ingredients.split(",")
        else:
            raise forms.ValidationError("Please enter ingredients for the recipe")

    def clean_instructions(self):
        if instructions := self.cleaned_data.get("instructions"):
            return instructions.split(",")
        else:
            raise forms.ValidationError("Please enter instructions for the recipe")
