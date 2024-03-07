from django.urls import path

from apps.tasks import views

urlpatterns = [
    path('', views.ListTask.as_view(), name='task-list'),
    path('<int:pk>/', views.RetrieveUpdateDestroyTask.as_view(), name='task-details')
]
