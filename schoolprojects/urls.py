from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='projects_list'),
    path('project/<str:project>/', views.project_detail, name='projects_detail'),
]
