<<<<<<< HEAD
from django.shortcuts import render


from rest_framework import viewsets
from .models import *
from .serializers import *
=======
from rest_framework import viewsets
from .models import *
from .serializers import *
from django.shortcuts import render, redirect
>>>>>>> 174518e34e0d9a80c29f3f23d280ed88bdee9ba4

def dashboard(request):
    return render(request, 'base.html')

class StudentViewSet(viewsets.ModelViewSet):
<<<<<<< HEAD
    queryset = se_students.objects.all()
=======
    queryset = ga_students.objects.all()
>>>>>>> 174518e34e0d9a80c29f3f23d280ed88bdee9ba4
    serializer_class = StudentSerializer


class SubjectViewSet(viewsets.ModelViewSet):
<<<<<<< HEAD
    queryset = cc_subjects.objects.all()
=======
    queryset = ga_subjects.objects.all()
>>>>>>> 174518e34e0d9a80c29f3f23d280ed88bdee9ba4
    serializer_class = SubjectSerializer


class AcademicYearViewSet(viewsets.ModelViewSet):
    queryset = ga_academicyears.objects.all()
    serializer_class = AcademicYearSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = ga_teacher.objects.all()
    serializer_class = TeacherSerializer


class SectionViewSet(viewsets.ModelViewSet):
    queryset = ga_sections.objects.all()
    serializer_class = SectionSerializer


class ExamViewSet(viewsets.ModelViewSet):
    queryset = ga_exam.objects.all()
    serializer_class = ExamSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = ga_assignment.objects.all()
    serializer_class = AssignmentSerializer


class StudentGradesViewSet(viewsets.ModelViewSet):
    queryset = ga_studentgrades.objects.all()
    serializer_class = StudentGradesSerializer


class GradesViewSet(viewsets.ModelViewSet):
    queryset = ga_grades.objects.all()
<<<<<<< HEAD
    serializer_class = GradesSerializer

# =================================
# COURSE & CURRICULUM MANAGEMENT
# =================================
=======
    serializer_class = GradesSerializer
>>>>>>> 174518e34e0d9a80c29f3f23d280ed88bdee9ba4
