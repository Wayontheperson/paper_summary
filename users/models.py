from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", 'Male')
        FEMALE = ("female", 'Female')

    first_name = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
    )
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender', 'email']


class UserManager(BaseUserManager):

    def create_user(self, username: str, email: str, first_name: str, last_name: str, password: str = None) -> User:
        if not username:
            raise ValueError('must have username')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            last_name=last_name,
            first_name=first_name,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username: str, email: str, first_name: str, last_name: str, password: str = None)-> User:
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            last_name=last_name,
            first_name=first_name,
        )
        user.is_superuser = True
        user.save()
        return user