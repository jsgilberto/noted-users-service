import uuid
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """ Custom user manager used to ignore username field
    """

    def create_user(self, email, first_name, last_name, password):
        if not email:
            raise ValueError('Email must be a valid email.')

        user = self.model(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, first_name=None, last_name=None):
        user = self.model(email=email, first_name=first_name, last_name=last_name,
            is_staff=True)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    """ Extending user base class
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField('email address', unique=True)
    
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    
    def __str__(self):
        return self.email



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs): 
    """ Creates a new token for every new user
    """
    if created:
        Token.objects.create(user=instance)

