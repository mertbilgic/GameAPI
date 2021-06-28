from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=self.normalize_email(username),
        )
        user.set_unusable_password()

        user.save(using=self._db)
        return user

    def create_superuser(self, email, username):
        user = self.create_user(username=username,email=email)
        user.is_admin = True
        user.set_unusable_password()
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True, blank=True, null=True, default=None)
    username= models.CharField(max_length=30,unique=True, blank=True, null=True)
    password = None

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']