# Django imports
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# Rest Framework Imports
from rest_framework import viewsets, permissions, status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Local imports
from .models import Recipe
from recipes.serializers import RecipeSerializer

# def ingredients_search(request, query):
#     recipes = Recipe.objects.filter(ingredients__icontains=query)
#     serializer = RecipeSerializer(recipes, many=True)
#     return JsonResponse(serializer.data, safe=False)

# def title_search(request, query):
#     recipes = Recipe.objects.filter(title__icontains=query)
#     serializer = RecipeSerializer(recipes, many=True)
#     return JsonResponse(serializer.data, safe=False)

def search(request, field, query):
    field = field.lower()
    recipes = None
    if field == 'title':
        recipes = Recipe.objects.filter(title__icontains=query)
    elif field == 'ingredients':
        recipes = Recipe.objects.filter(ingredients__icontains=query)
    elif field == 'directions':
        recipes == Recipe.objects.filter(directions__icontains=query)
    
    if recipes is None:
        return HttpReponseBadRequest('<h1>Invalid Search Field</h1>')
    
    serializer = RecipeSerializer(recipes, many=True)
    return JsonResponse(serializer.data, safe=False)

def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/detail.html', {'recipe': recipe})

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by('-created_date')
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['GET', 'POST'])
def recipe_list(request):
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = RecipeSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

@api_view(['GET', 'PUT','DELETE'])
def recipe_detail(request, recipe_id):
    try:
        recipe = Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = RecipeSerializer(recipe)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        recipe.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)