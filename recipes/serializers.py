from .models import Recipe
from rest_framework import serializers

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields =  ['id', 'link', 'title', 'ingredients', 'directions', 'source', 'created_date']