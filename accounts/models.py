from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from .enums import UserRoles
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .managers import DirectorsManager, ManagersManager, TeachersManager, StudetnsManager
from .services import location_image, validate_image, custom_validator


class User(AbstractBaseUser):

    phone_regex = RegexValidator(regex=r'^998[0-9]{2}[0-9]{7}$',
                                 message="Faqat O`zbekiston mobil raqamlari tasdiqlanadi('+' belgisiz!)")
    username = None
    phone = models.CharField(_('Telefon raqam'), validators=[phone_regex], max_length=17, unique=True)
    first_name = models.CharField(verbose_name='Name', max_length=50)
    last_name = models.CharField(verbose_name='Surname', max_length=50)
    email = models.EmailField(max_length=50, unique=True, blank=True, null=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=20, choices=UserRoles.choices(), blank=True, null=True)
    image = models.FileField(upload_to=location_image, validators=[validate_image, custom_validator],
                             help_text='Maximum file size allowed is 2Mb')

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email', 'password']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Director(User):
    objects = DirectorsManager()

    class Meta:
        proxy = True


class Manager(User):
    objects = ManagersManager()

    class Meta:
        proxy = True


class Teacher(User):
    objects = TeachersManager()

    class Meta:
        proxy = True


class Student(User):
    objects = StudetnsManager()

    class Meta:
        proxy = True
