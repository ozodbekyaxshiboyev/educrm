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
    creator = models.ForeignKey(User,on_delete=models.SET_NULL,validators=[directormanager], null=True,related_name='coursecreator')
    name = models.CharField(max_length=50)
    duration = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)


class Language(BaseModel):
    creator = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, related_name='languagecreator')
    name = models.CharField(max_length=50, choices=Languages.choices())


class Group(BaseModel):
    creator = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, related_name='groupcreator')
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='groupcourse')
    teacher = models.ForeignKey(User, on_delete=models.PROTECT,related_name='groupteacher')   #todo Teacher modeligi ulanmasmikan
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True,related_name='grouplanguage')
    count_student = models.PositiveIntegerField()
    max_count_student = models.PositiveIntegerField()


class GroupItem(BaseModel):
    creator = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, related_name='groupitemcreator')
    student = models.ForeignKey(User, on_delete=models.CASCADE,related_name='groupitemstudent')
    group = models.ForeignKey(Group, on_delete=models.CASCADE,related_name='groupitemgroup')


class Lesson(BaseModel):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='lessoncreator')  #todo Teacher
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='lessoncourse')
    file = models.FileField(upload_to='lesson_files')    #todo


class LessonItem(BaseModel):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,related_name='lessonitemlesson')
    group = models.ForeignKey(Group, on_delete=models.CASCADE,related_name='lessonitemgroup')



class Homework(BaseModel):
    creator = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, related_name='homeworkcreator')  #todo
    lessonitem = models.ForeignKey(LessonItem, on_delete=models.CASCADE,related_name='homeworklessonitem')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='homeworkteacher')
    text = models.TextField(max_length=1000, null=True, blank=True)
    file = models.FileField(upload_to='homeworks', null=True, blank=True)


class HomeworkAnswer(BaseModel):
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,related_name='homeworkanswerstudent')
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE,related_name='homeworkasnwerhomework')
    text = models.TextField(max_length=1000, null=True, blank=True)
    file = models.FileField(upload_to='homeworks', null=True, blank=True)


class HomeworkResult(BaseModel):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE,related_name='homeworkresultteacher')
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,related_name='homeworkresultstudent')
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE,related_name='homeworkresulthomework')
    mark = models.PositiveIntegerField()


class Exam(BaseModel):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='examcreator')
    text = models.TextField(max_length=1000, null=True, blank=True)
    file = models.FileField(upload_to='homeworks', null=True, blank=True)


class ExamItem(BaseModel):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE,related_name='examitemexam')
    group = models.ForeignKey(Group, on_delete=models.CASCADE,related_name='examitemgroup')
    start_date = models.DateField()
    end_date = models.DateField()


class ExamResult(BaseModel):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE,related_name='examresultexam')
    student = models.ForeignKey(User, on_delete=models.CASCADE,related_name='examresultstudent')
    mark = models.PositiveIntegerField()


class Task(BaseModel):
    creator = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, related_name='taskcreator')
    text = models.TextField(max_length=1000, null=True, blank=True)
    file = models.FileField(upload_to='homeworks', null=True, blank=True)


class TaskItem(BaseModel):
    creator = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, related_name='taskitem')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,related_name='taskitemuser')
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True,related_name='taskitemgroup')
    task = models.ForeignKey(Task, on_delete=models.CASCADE,related_name='taskitemtask')
    start_date = models.DateField()
    end_date = models.DateField()


class TaskResult(BaseModel):
    creator = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, related_name='taskresult')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,related_name='taskresultuser')
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True,related_name='taskresultgroup')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='taskresulttask')
    is_done = models.BooleanField(default=True)