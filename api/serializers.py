from rest_framework import serializers
from assessments.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = se_students
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = cc_subjects
        fields = '__all__'


class AcademicYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = cc_academicyears
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