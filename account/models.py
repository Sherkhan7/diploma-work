from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class User(AbstractUser):
    PROFESSOR = 1
    STUDENT = 2
    ROLE_CHOICES = (
        (PROFESSOR, 'Professor'),
        (STUDENT, 'Student'),
    )

    first_name = models.CharField(_('first name'), max_length=150)
    last_name = models.CharField(_('last name'), max_length=150)
    email = models.EmailField(_('email address'), unique=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_absolute_url(self):
        return reverse('account:detail', kwargs={'slug': self.username})
