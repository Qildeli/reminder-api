from django.urls import path
from apps.users import views



urlpatterns = [
    path('register/', views.RegisterAPI.as_view()),
    path('', views.UserList.as_view()),
    path('<int:pk>/', views.UserDetail.as_view()),
]