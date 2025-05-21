from django.urls import path
from .views import*
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tasks/', taskcreate, name='task_list_create'),
    path('tasks/<int:pk>/', task_detail, name='task_detail'),
]
