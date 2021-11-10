from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('access/', views.MyTokenObtainPairView.as_view(), name='access'),
]
