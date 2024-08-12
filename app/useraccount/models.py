"""User account database model"""

import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    UserManager,
)
from django.db import models


class CustomUserManager(UserManager):
    """Manager for users"""

    def _create_user(
        self,
        name,
        email,
        password,
        **extra_fields,
    ):
        """Create, save and return new user"""

        if not email:
            raise ValueError("User must provide email address!")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(
        self,
        name=None,
        email=None,
        password=None,
        **extra_fields,
    ):
        """Create and return regular user"""

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(name, email, password, **extra_fields)

    def create_superuser(
        self,
        name,
        email,
        password,
        **extra_fields,
    ):
        """Create and return new superuser"""

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self._create_user(name, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.ImageField(upload_to="uploads/avatars/")
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = [
        "name",
    ]
