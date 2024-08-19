from django import forms

from . import models


class PropertyForm(forms.ModelForm):
    class Meta:
        model = models.Property
        fields = (
            "title",
            "description",
            "price_per_night",
            "bedrooms",
            "guests",
            "country",
            "country_code",
            "category",
            "image",
        )
