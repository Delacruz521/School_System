from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
<<<<<<< HEAD
        model = se_students
=======
        model = ga_students
>>>>>>> 174518e34e0d9a80c29f3f23d280ed88bdee9ba4
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
<<<<<<< HEAD
        model = cc_subjects
=======
        model = ga_subjects
>>>>>>> 174518e34e0d9a80c29f3f23d280ed88bdee9ba4
        fields = '__all__'


class AcademicYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = ga_academicyears
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = ga_teacher
        fields = '__all__'


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ga_sections
        fields = '__all__'


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ga_exam
        fields = '__all__'


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ga_assignment
        fields = '__all__'


class StudentGradesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ga_studentgrades
        fields = '__all__'


class GradesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ga_grades
        fields = '__all__'