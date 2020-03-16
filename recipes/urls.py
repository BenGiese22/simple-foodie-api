from django.urls import include, path
from recipes import views

app_name = 'recipes'

urlpatterns = [
    # ex: /recipes/
    # path('', views.index, name='index'),
    # ex: /recipes/5/
    path('<int:recipe_id>/', views.detail, name='detail'),

    path('recipes-api/', views.recipe_list),

    path('recipes-api/<int:recipe_id>/', views.recipe_detail),
]
