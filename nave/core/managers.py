from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """
    Custom manager for new core.User model.
    """

    use_in_migrations = True

    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password
        """
        if not email:
            raise ValueError(_("Users must have an email address"))

        user = self.model(email=self.normalize_email(email),)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email and password
        """
        user = self.create_user(email, password=password,)
        user.is_staff = True
        user.save(using=self._db)
        return user
