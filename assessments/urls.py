from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import *

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'academic-years', AcademicYearViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'sections', SectionViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'student-grades', StudentGradesViewSet)
router.register(r'grades', GradesViewSet)

urlpatterns = [
    path('', views.dashboard, name='dashboard'),   # 🖥️ HTML DASHBOARD
    path('api/', include(router.urls)),            # 🔌 API ROUTER
]