from django.urls import path, re_path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('add/', views.addrecipe, name='add'),
    re_path('(?P<recipe_id>[0-9]+)/$', views.recipe_details, name="recipe_details"),
]
