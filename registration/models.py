from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Rollar'

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.PROTECT, null=True, verbose_name='Foydalanuvchi roli')

    def __str__(self):
        return self.username
