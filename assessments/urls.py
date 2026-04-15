<<<<<<< HEAD
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
=======
from rest_framework.routers import DefaultRouter
from django.urls import path, include
>>>>>>> 174518e34e0d9a80c29f3f23d280ed88bdee9ba4
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
<<<<<<< HEAD
    path('', views.dashboard, name='dashboard'),   # 🖥️ HTML DASHBOARD
    path('api/', include(router.urls)),            # 🔌 API ROUTER
=======
    path('', dashboard, name='dashboard'),
    path('api/', include(router.urls)),
>>>>>>> 174518e34e0d9a80c29f3f23d280ed88bdee9ba4
]