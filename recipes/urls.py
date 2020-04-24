from django.urls import include, path
from recipes import views

app_name = 'recipes'

urlpatterns = [
    # Landing Page
    path('', views.landing, name='landing'),

    # Detail View
    path('<int:recipe_id>/', views.detail, name='detail'),

    # Search Query View
    path('recipes-api/<str:field>/<str:query>/', views.search, name='search'),

    # Standard Recipes Views
    path('recipes-api/', views.recipe_list),
    path('recipes-api/<int:recipe_id>/', views.recipe_detail),
]
