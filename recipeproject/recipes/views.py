from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Recipe
from django.http import Http404

# Create your views here.
@login_required # decorator that forces user to be logged in to proceed on this page
def addrecipe(request):
    if request.method == 'POST':
        # must register the Recipe model in admin.py, so we can check the entries using /admin
        if request.POST['name'] and request.POST['content']:
            recipe = Recipe()
            recipe.name = request.POST['name']
            recipe.content = request.POST['content']
            recipe.add_date = timezone.datetime.now()
            recipe.author = request.user
            recipe.save()
            # should go to home page once we have it
            return redirect('home')
        else:
            return render(request, 'recipes/add.html', {'error':'Error: Please specify both fields'})
    else:
        if request.method == 'GET':
            return render(request, 'recipes/add.html')

def home(request):
    # get all the recipes from the database
    recipes = Recipe.objects.order_by('-add_date')
    # pass the db objects to the templates using the third parameter
    return render(request, 'recipes/home.html', {'recipes':recipes })

def recipe_details(request, recipe_id):
    # retrive from db, given the id
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/recipe_details.html', {'recipe':recipe})

def deleterecipe(request):
    if request.method == 'POST':
        try:
            if request.POST['recipe_del_id']:
                recipe_del_id = request.POST['recipe_del_id']
                recipe = get_object_or_404(Recipe, pk=recipe_del_id)
                recipe.delete()
                return render(request, 'recipes/delete.html', {'error':'Deletion was successful !'})
            else:
                return render(request, 'recipes/delete.html', {'error':'Error: Please specify a recipe id'})
        except Http404:
            return render(request, 'recipes/delete.html', {'error':'Error: The id was not found'})
    else:
        if request.method == 'GET':
            return render(request, 'recipes/delete.html')
