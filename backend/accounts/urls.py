from django.urls import path

from . import views


urlpatterns = [
    path('auth/login/', views.LoginView.as_view(), name='login'),
    path('auth/register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.UserList.as_view(), name='profile-list'),
    path('profile/<int:pk>/', views.UserDetail.as_view(), name='profile-detail'),
]
