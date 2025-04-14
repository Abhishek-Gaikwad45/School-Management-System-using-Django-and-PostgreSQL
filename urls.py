

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, StudentViewSet, TeacherViewSet, AttendanceViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'attendance', AttendanceViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
