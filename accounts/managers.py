from django.db import models
from .enums import UserRoles
from django.contrib.auth.models import BaseUserManager


class DirectorsManager(BaseUserManager):
    def get_queryset(self):
        return super(DirectorsManager, self).get_queryset().filter(
            role=UserRoles.director.value)

    def create(self, **kwargs):
        kwargs.update({'role': UserRoles.director.value})
        return super(DirectorsManager, self).create(**kwargs)


class ManagersManager(models.Manager):
    def get_queryset(self):
        return super(ManagersManager, self).get_queryset().filter(
            role=UserRoles.manager.value)

    def create(self, **kwargs):
        kwargs.update({'role': UserRoles.manager.value})
        return super(ManagersManager, self).create(**kwargs)


class TeachersManager(models.Manager):
    def get_queryset(self):
        return super(TeachersManager, self).get_queryset().filter(
            role=UserRoles.teacher.value)

    def create(self, **kwargs):
        kwargs.update({'role': UserRoles.teacher.value})
        return super(TeachersManager, self).create(**kwargs)



class StudetnsManager(models.Manager):
    def get_queryset(self):
        return super(StudetnsManager, self).get_queryset().filter(
            role=UserRoles.student.value)

    def create(self, **kwargs):
        kwargs.update({'role': UserRoles.student.value})
        return super(StudetnsManager, self).create(**kwargs)