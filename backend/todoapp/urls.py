from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverView, name="api-overview"),
    path('todo-list/', views.apiListView, name="api-list"),
    path('todo-detail/<int:id>', views.apiDetailView, name="api-detail"),        
]