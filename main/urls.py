from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, home, delete_task, toggle_task

router = DefaultRouter()
router.register('api/tasks', TaskViewSet)

urlpatterns = [
    path('', home),
    path('delete/<int:pk>/', delete_task),
    path('toggle/<int:pk>/', toggle_task),
    path('', include(router.urls)),
]