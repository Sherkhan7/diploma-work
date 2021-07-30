from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    PROFESSOR = 1
    STUDENT = 2
    ROLE_CHOICES = (
        (PROFESSOR, 'Professor'),
        (STUDENT, 'Student'),
    )

    email = models.EmailField(_('email address'), blank=True, unique=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=False, null=True)

    USERNAME_FIELD = 'email'
