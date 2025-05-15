from django import forms
from .models import Calorie

class CalorieForm(forms.ModelForm):
    class Meta:
        model = Calorie
        fields = ['name', 'Vegetarian', 'Took_water_today', 'food_item']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-md text-black'}),
            'vegetarian': forms.CheckboxInput(attrs={'class': 'h-5 w-5'}),
            'took_water_today': forms.CheckboxInput(attrs={'class': 'h-5 w-5'}),
        }
        