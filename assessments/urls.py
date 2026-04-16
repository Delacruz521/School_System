from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from api.views import *

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
    
    # EXAM URLS
    path('create-exam/', create_exam, name='create-exam'),
    
    # SUBJUCT URLS

    # API URL
    path('api/', include(router.urls)),            # API ROUTER
]