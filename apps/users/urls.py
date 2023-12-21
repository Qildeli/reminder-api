from django.urls import path
from apps.users import views



urlpatterns = [
    path('register/', views.RegisterAPI.as_view()),
]