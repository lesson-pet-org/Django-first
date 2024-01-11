from django.db import models

from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise TypeError('Users must have a username.')

        if not email:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name='Логин',
        max_length=255,
        unique=True
    )
    email = models.EmailField(
        verbose_name='email',
        max_length=100,
        unique=True
    )
    is_active = models.BooleanField(
        verbose_name='Является активным',
        default=True
    )
    is_staff = models.BooleanField(
        verbose_name='Является админом',
        default=False
    )
    created_at = models.DateTimeField(
        verbose_name='Дата регистрации',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата обновления',
        auto_now=True
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'