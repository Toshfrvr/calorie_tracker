from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CalorieForm
from .models import Calorie
# Create your views here.

def index(request):

    return HttpResponse('Hello, world! This is the calorie tracker app.')


def add_calorie(request):
    if request.method == 'POST':
        form = CalorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calorie_list')  # Make sure 'calories_list' is the name of your URL pattern for the calorie list view
    else:
        form = CalorieForm()

    return render(request, 'calorie.html', {'form': form})

def get_calories(request):
    if request.method == 'GET':
        calories = Calorie.objects.all()

        return render(request, 'calories_list.html', {'calories': calories})
    else:
        return HttpResponse('Invalid request method.')