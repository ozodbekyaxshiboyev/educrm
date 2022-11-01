from django.db import models
from accounts.models import User
from django.db.models import Model
from django.core.exceptions import ValidationError
# from .services import location_image, validate_image, custom_validator
from .enums import Languages
from .services import directormanager



class BaseModel(models.Model):
    created_date = models.DateField(auto_now=True)
    updated_date = models.DateField(auto_now=True)
    is_deleted = models.BooleanField(default=False,blank=True, null=True)

    class Meta:
        abstract = True



class Course(BaseModel):
    creator = models.ForeignKey(User,on_delete=models.SET_NULL,validators=[directormanager], null=True,related_name='courses')
    name = models.CharField(max_length=50)
    duration = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)


class Language(BaseModel):
    creator = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, related_name='languages')
    name = models.CharField(max_length=50, choices=Languages.choices())


class Group(BaseModel):
    creator = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, related_name='groups')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.PROTECT)   #todo Teacher modeligi ulanmasmikan
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    count_student = models.PositiveIntegerField()
    max_count_student = models.PositiveIntegerField()


class GroupItem(BaseModel):
    creator = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, related_name='groupitem')
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Lesson(BaseModel):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='lesson')  #todo Teacher
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    file = models.FileField(upload_to='lesson_files')    #todo


class LessonItem(BaseModel):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)



class Homework(BaseModel):
    creator = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, related_name='homework')  #todo
    lessonitem = models.ForeignKey(LessonItem, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='homework-teacher')
    text = models.TextField(max_length=1000, null=True, blank=True)
    file = models.FileField(upload_to='homeworks', null=True, blank=True)


class HomeworkAnswer(BaseModel):
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000, null=True, blank=True)
    file = models.FileField(upload_to='homeworks', null=True, blank=True)


class HomeworkResult(BaseModel):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    mark = models.PositiveIntegerField()


class Exam(BaseModel):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='exam')
    text = models.TextField(max_length=1000, null=True, blank=True)
    file = models.FileField(upload_to='homeworks', null=True, blank=True)


class ExamItem(BaseModel):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()


class ExamResult(BaseModel):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.PositiveIntegerField()


class Task(BaseModel):
    creator = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, related_name='task')
    text = models.TextField(max_length=1000, null=True, blank=True)
    file = models.FileField(upload_to='homeworks', null=True, blank=True)


class TaskItem(BaseModel):
    creator = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, related_name='taskitem')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()


class TaskResult(BaseModel):
    creator = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, related_name='taskresult')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=True)