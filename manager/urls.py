from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.tasks_list_create),
    path('tasks/<str:task_id>/', views.task_detail),
    path('categories/', views.categories_list_create),
    path('categories/<str:category_id>/', views.category_detail),
]
