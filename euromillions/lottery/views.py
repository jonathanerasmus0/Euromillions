from django.shortcuts import render

# Create your views here.
import random
from django.http import JsonResponse
from django.shortcuts import render


# List of the most frequently drawn EuroMillions numbers
most_drawn_numbers = [17, 20, 21, 23, 42]

def generate_numbers(request):
    selected_numbers = random.sample(most_drawn_numbers, 5)
    return JsonResponse({'numbers': selected_numbers})

def index(request):
    return render(request, 'lottery/index.html')
