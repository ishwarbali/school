from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='projects_list'),
    path('project/<str:name>/', views.project_detail, name='projects_detail'),
    
]
