from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View
from  django.http import HttpResponse
from .models import Food

class FoodListView(View):
    template_name = 'food-list.html'

    def get(self, request):
        foods = Food.objects.all()
        return render(request, self.template_name, {'foods:':foods})