from django.db import models

# Create your models here.

# ================================
# STUDENT INFORMATION
# ================================
class se_students(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    extension_name = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    civil_status = models.CharField(max_length=20)
    place_of_birth = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    mother_toungue = models.CharField(max_length=50)
    is_indigenous = models.BooleanField(default=False)
    is_4ps_beneficiary = models.BooleanField(default=False)

    class Meta:
        db_table = 'se_students'

# ================================
# ASSESSMENT & GRADING
# ================================


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
    subject_id = models.ForeignKey('cc_subjects', on_delete=models.CASCADE)
    ay = models.ForeignKey('cc_academicyears', on_delete=models.CASCADE)

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
    subject_id = models.ForeignKey('cc_subjects', on_delete=models.CASCADE)
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
    student_id = models.ForeignKey('se_students', on_delete=models.CASCADE)
    assessment = models.ForeignKey('ga_exam', on_delete=models.CASCADE, null=True, blank=True)

    ASSESSMENT_TYPE = [
        ('Exam', 'Exam'),
        ('Assignment', 'Assignment')
    ]

    assessment_type = models.CharField(max_length=20, choices=ASSESSMENT_TYPE, null=True, blank=True)
    raw_score = models.PositiveIntegerField()
    percentage_score = models.FloatField()
    date_recorded = models.DateField(auto_now_add=True)
    is_late_submission = models.BooleanField(default=False)

    class Meta:
        db_table = 'ga_studentgrades'

class ga_grades(models.Model):
    summary_grade_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey('se_students', on_delete=models.CASCADE)
    subject_id = models.ForeignKey('cc_subjects', on_delete=models.CASCADE)
    ay_id = models.ForeignKey('cc_academicyears', on_delete=models.CASCADE)
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
    student_id = models.ForeignKey('se_students', on_delete=models.CASCADE)
    ay = models.ForeignKey('cc_academicyears', on_delete=models.CASCADE)
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

    student = models.ForeignKey('se_students', on_delete=models.CASCADE)

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


        

# ================================
# COURSE & CURRICULUM MANAGEMENT
# ================================

class cc_academicyears(models.Model):
    ay_id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=20)

    class Meta:
        db_table = 'cc_academicyears'

class cc_subjects(models.Model):
    subject_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'ga_subjects'


class cc_courses(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_code = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    description = models.TextField()
    years_to_complete = models.IntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'ga_courses'


class cc_curriculum(models.Model):
    curriculum_id = models.AutoField(primary_key=True)
    course = models.ForeignKey('cc_courses', on_delete=models.CASCADE)
    effective_year_start = models.IntegerField()
    effective_year_end = models.IntegerField()
    description = models.TextField()
    is_current_standard = models.BooleanField(default=True)

    class Meta:
        db_table = 'ga_curriculum'


class cc_prerequisites(models.Model):
    prereq_id = models.AutoField(primary_key=True)
    subject = models.ForeignKey('cc_subjects', on_delete=models.CASCADE)
    required_subject = models.ForeignKey(
        'cc_subjects',
        on_delete=models.CASCADE,
        related_name='required_for'
    )
    min_grade_required = models.FloatField()

    class Meta:
        db_table = 'cc_prerequisites'

class cc_classsections(models.Model):
    section_id = models.AutoField(primary_key=True)
    ay = models.ForeignKey('cc_academicyears', on_delete=models.CASCADE)
    course = models.ForeignKey('cc_courses', on_delete=models.CASCADE)
    grade_level_or_year = models.CharField(max_length=20)
    section_name = models.CharField(max_length=50)
    max_capacity = models.IntegerField()
    adviser = models.ForeignKey('ga_teacher', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'cc_classsections'


class cc_classschedules(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    section = models.ForeignKey('cc_classsections', on_delete=models.CASCADE)
    subject = models.ForeignKey('cc_subjects', on_delete=models.CASCADE)
    faculty = models.ForeignKey('ga_teacher', on_delete=models.SET_NULL, null=True)
    day_of_week = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        db_table = 'cc_classschedules'


class cc_roomassignments(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_number = models.CharField(max_length=20)
    building_name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=20)
    capacity = models.IntegerField()
    is_airconditioned = models.BooleanField(default=False)

    class Meta:
        db_table = 'cc_roomassignments'


class cc_coursematerials(models.Model):
    material_id = models.AutoField(primary_key=True)
    subject = models.ForeignKey('cc_subjects', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    file_type = models.CharField(max_length=20)
    file_url = models.URLField()
    author = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cc_coursematerials'


class cc_coursenotes(models.Model):
    note_id = models.AutoField(primary_key=True)
    course = models.ForeignKey('cc_courses', on_delete=models.CASCADE)
    user = models.ForeignKey('ga_teacher', on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cc_coursenotes'