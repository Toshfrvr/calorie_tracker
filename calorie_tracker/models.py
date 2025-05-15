from django.db import models

# Create your models here.

class Calorie(models.Model):
    FOOD_ITEM_CHOICES = [
        ('fruit', 'Fruit'),
        ('vegetable', 'Vegetable'),
        ('grain', 'Grain'),
        ('protein', 'Protein'),
        ('dairy', 'Dairy'),
    ]
    name = models.CharField(max_length=100)
    Vegetarian = models.BooleanField(default=False)
    Took_water_today = models.BooleanField(default=False)
    food_item = models.CharField(max_length=50, choices=FOOD_ITEM_CHOICES)

    def __str__(self):
        return self.name 
