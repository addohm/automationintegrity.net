from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import ugettext_lazy as _
from customers import models as customers_models


class TravelModel(models.Model):
    mileageRate = models.DecimalField(max_digits=4, decimal_places=3)

    def __str__(self):
        return '%s' % (self.mileageRate)

    class Meta:
        verbose_name = "Current Federal Milage Rate"
        # verbose_name_plural = "Milage"


class UserManager(BaseUserManager):
    def create_user(self, username, email, firstName, lastName, company, phone, password=None, **kwargs):
        #   email = self.normalize_email(email)
        #   user = self.model(email=email, **kwargs)
        #   user.firstName = firstName
        #   user.lastName = lastName
        #   user.company = company
        #   user.phone = phone
        """
        Creates and saves a User with the given email, first name, last name,
        company, phone, and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            firstName=firstName,
            lastName=lastName,
            company=company,
            phone=phone
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, firstName, lastName, password=None, **kwargs):
        # user = self.create_user(**kwargs)
        #   email = self.normalize_email(email)
        #   user = self.model(email=email, **kwargs)
        #   user.firstName = firstName
        #   user.lastName = lastName
        """
        Creates and saves a User with the given email, first name, last name,
        company, phone, and password.
        """
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            firstName=firstName,
            lastName=lastName,
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user


# class AliasField(models.Field):
#     def contribute_to_class(self, cls, name, virtual_only=False):
#         super().contribute_to_class(cls, name, virtual_only=True)
#         setattr(cls, name, self)

#     def __get__(self, instance, instance_type=None):
#         return getattr(instance, self.db_column)


class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('Username'), max_length=150, unique=True, null=False, blank=False)
    email = models.EmailField(_('E-mail Address'), max_length=255, unique=True)
    firstName = models.CharField(_('First Name'), max_length=50, blank=False, null=False)
    lastName = models.CharField(_('Last Name'), max_length=50, blank=False, null=False)
    # company = models.ForeignKey(customers_models.CompanyModel, on_delete=models.PROTECT, null=False)
    # phone = models.ForeignKey(customers_models.PhoneModel, on_delete=models.PROTECT, null=False)
    company = models.ForeignKey(customers_models.CompanyModel, on_delete=models.PROTECT, null=True)
    phone = models.ForeignKey(customers_models.PhoneModel, on_delete=models.PROTECT, null=True)
    is_admin = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin '
            'site.'
        )
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as '
            'active. Unselect this instead of deleting accounts.'
        )
    )
    #      username = AliasField(db_column='email')

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'firstName', 'lastName']

    class Meta(object):
        ordering = ['firstName']
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return '%s - %s %s - %s - %s' % (self.company, self.firstName, self.lastName, self.email, self.phone)

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
