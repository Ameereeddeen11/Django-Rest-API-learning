from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverView, name="api-overview"),
    path('todo-list/', views.apiListView, name="api-list"),
    path('todo-detail/<int:id>', views.apiDetailView, name="api-detail"),        
    path('todo-create/', views.apiPost, name="api-create"),
    path('todo-update/<str:pk>/', views.apiUpdate, name="api-update"),
    path('todo-delete/<int:id>/', views.apiDelete, name="api-delete"),
]