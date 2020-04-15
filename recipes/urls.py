from django.urls import include, path
from recipes import views

app_name = 'recipes'

urlpatterns = [

    # Detail View
    path('<int:recipe_id>/', views.detail, name='detail'),

    # Search Query Views
    path('recipes-api/<str:field>/<str:query>/', views.search, name='search'),

    # path('recipes-api/title/<str:query>/', views.title_search, name='title_search'),
    # path('recipes-api/ingredients/<str:query>/', views.ingredients_search, name='ingredients_search'),

    # Standard Recipes Views
    path('recipes-api/', views.recipe_list),
    path('recipes-api/<int:recipe_id>/', views.recipe_detail),
]
