from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add_calorie/', add_calorie, name='add_calorie'),
    path('get_calories/', get_calories, name='calorie_list'),
]