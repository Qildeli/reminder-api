from django.urls import path

from apps.todo import views

urlpatterns = [
    path('', views.ListTask.as_view(), name='todo-list'),
    path('<int:pk>/', views.RetrieveUpdateDestroyTask.as_view(), name='todo-details')
]
