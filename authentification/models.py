from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class CustomUser(AbstractUser):
    date_birth = models.DateField(null=True, blank=True)
    is_instructor = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set_permissions')


    def __str__(self):
        return self.username
    