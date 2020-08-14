from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Inherited User from AbstractBaseUser to allow login
    with e-mail.
    """

    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={"unique": _("A user with that email already exists."),},
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("A staff user can login the admin site"),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Users with not active status cannot login the site."
            "Use this in case of users that want to delete their profiles"
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self) -> str:
        """
        The user is identified by the email address.
        """
        return self.email

    def get_short_name(self) -> str:
        """
        The user is identified by the email address.
        """
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Send an email to this user.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
