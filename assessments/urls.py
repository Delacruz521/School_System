from rest_framework.routers import DefaultRouter
from django.urls import path, include
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
    path('', dashboard, name='dashboard'),
    path('api/', include(router.urls)),
]