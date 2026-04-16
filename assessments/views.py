from django.shortcuts import render, redirect
from .models import *
from .forms import *

def dashboard(request):
    return render(request, 'base.html')

# ========
# CRUD GRADE & ASSESSMENT
# ========

def create_exam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exam.html')
    else:
        form = ExamForm()
    return render(request, 'exam/exam.html', {'form': form})

# =================================
# COURSE & CURRICULUM MANAGEMENT
# =================================
