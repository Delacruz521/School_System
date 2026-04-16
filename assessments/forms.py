from django import forms
from .models import *

class SubjectForm(forms.ModelForm):
    class Meta:
        model = cc_subjects
        fields = [
            'subject_id',
            'name'
        ]

class ExamForm(forms.ModelForm):
    class Meta:
        model = ga_exam
        fields = [
            'subject_id',
            'ay',
            'grading_period',
            'exam_type',
            'max_score',
            'exam_date'
        ]

        widgets = {
            'exam_date': forms.DateInput(attrs={'type': 'date'}),
        }
