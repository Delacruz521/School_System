from django.db import models

# Create your models here.

class ga_students(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'ga_students'

class ga_subjects(models.Model):
    subject_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'ga_subjects'

class ga_academicyears(models.Model):
    ay_id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=20)

    class Meta:
        db_table = 'ga_academicyears'


class ga_teacher(models.Model):
    faculty_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'ga_teacher'

class ga_faculty(models.Model):
    faculty_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'ga_faculty'

class ga_sections(models.Model):
    section_id = models.AutoField(primary_key=True)
    section_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'ga_sections'

class ga_exam(models.Model):
    exam_id = models.AutoField(primary_key=True)
    subject_id = models.ForeignKey('ga_subjects', on_delete=models.CASCADE)
    ay = models.ForeignKey('ga_academicyears', on_delete=models.CASCADE)

    GRADING_PERIOD = [
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
        ('4th', '4th'),
    ]

    grading_period = models.CharField(max_length=3, choices=GRADING_PERIOD)

    EXAM_TYPE = [
        ('Quarterly', 'Quarterly'),
        ('Periodic', 'Periodic'),
    ]
    exam_type = models.CharField(max_length=20, choices=EXAM_TYPE)
    max_score = models.PositiveIntegerField()
    exam_date = models.DateField()

    class Meta:
        db_table = 'ga_exam'

class ga_assignment(models.Model):
    assignment_id = models.AutoField(primary_key=True)
    subject_id = models.ForeignKey('ga_subjects', on_delete=models.CASCADE)
    section_id = models.ForeignKey('ga_sections', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    CATEGORY = [
        ('Written Work', 'Written Work'),
        ('Performance Task', 'Performance Task'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY)
    raw_score = models.PositiveIntegerField()
    weight = models.FloatField()
    due_date = models.DateField()

    class Meta:
        db_table = 'ga_assignment'


class ga_rubrics(models.Model):
    rubric_id = models.AutoField(primary_key=True)
    assignment_id = models.ForeignKey('ga_assignment', on_delete=models.CASCADE)
    criteria_name = models.CharField(max_length=100)
    description = models.TextField()
    max_points_per_criteria = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        db_table = 'ga_rubrics'

class ga_studentgrades(models.Model):
    grade_record_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey('ga_students', on_delete=models.CASCADE)
    exam = models.ForeignKey('ga_exam', on_delete=models.CASCADE, null=True, blank=True)
    assignment = models.ForeignKey('ga_assignment', on_delete=models.CASCADE, null=True, blank=True)
    raw_score = models.PositiveIntegerField()
    percentage_score = models.FloatField()
    date_recorded = models.DateField(auto_now_add=True)
    is_late_submission = models.BooleanField(default=False)

    class Meta:
        db_table = 'ga_studentgrades'

class ga_grades(models.Model):
    summary_grade_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey('ga_students', on_delete=models.CASCADE)
    subject_id = models.ForeignKey('ga_subjects', on_delete=models.CASCADE)
    ay_id = models.ForeignKey('ga_academicyears', on_delete=models.CASCADE)
    GRADING_PERIOD = [
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
        ('4th', '4th'),
    ]

    grading_period = models.CharField(max_length=3, choices=GRADING_PERIOD)
    initial_grade = models.FloatField()
    transmuted_grade = models.FloatField()
    is_passed = models.BooleanField(default=False)

    class Meta:
        db_table = 'ga_grades'

class ga_teacherremarks(models.Model):
    remark_id = models.AutoField(primary_key=True)
    summary_grade_id = models.ForeignKey('ga_grades', on_delete=models.CASCADE)
    faculty_id = models.ForeignKey('ga_faculty', on_delete=models.CASCADE)
    narrative_remark = models.TextField()
    core_values_rating = models.CharField(max_length=100)
    observed_values = models.TextField()

    class Meta:
        db_table = 'ga_teacherremarks'

class ga_gradescale(models.Model):
    scale_id = models.AutoField(primary_key=True)
    min_raw_score = models.FloatField()
    max_raw_score = models.FloatField()
    transmuted_grade = models.FloatField()
    description = models.CharField(max_length=100)

    class Meta:
        db_table = 'ga_gradescale'

class ga_reportcards(models.Model):
    card_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey('ga_students', on_delete=models.CASCADE)
    ay = models.ForeignKey('ga_academicyears', on_delete=models.CASCADE)
    general_average = models.FloatField()   
    attendance_present = models.IntegerField()
    attendance_absent = models.IntegerField()

    STATUS = [
        ('Promoted', 'Promoted'),
        ('Retained', 'Retained'),
    ]

    status = models.CharField(max_length=10, choices=STATUS)
    issued_date = models.DateField()

    class Meta:
        db_table = 'ga_reportcards'

class ga_transcripts(models.Model):
    transcript_id = models.AutoField(primary_key=True)

    student = models.ForeignKey('ga_students', on_delete=models.CASCADE)

    total_units_earned = models.IntegerField()
    gpa = models.FloatField()
    graduation_date = models.DateField()

    is_official_copy = models.BooleanField(default=False)
    remarks = models.TextField()

    class Meta:
        db_table = 'ga_transcripts'

class ga_gradeshistory(models.Model):
    history_id = models.AutoField(primary_key=True)

    summary_grade = models.ForeignKey('ga_grades', on_delete=models.CASCADE)

    old_grade = models.FloatField()
    new_grade = models.FloatField()

    changed_by = models.ForeignKey('ga_teacher', on_delete=models.SET_NULL, null=True)

    reason_for_change = models.TextField()
    change_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ga_gradeshistory'