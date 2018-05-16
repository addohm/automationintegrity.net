from django.db import models
from django.core.validators import RegexValidator
from main import models as main_models
from django.utils.translation import ugettext_lazy as _


'''
The address model is just a generic address container
'''


class AddressModel(models.Model):
    street1 = models.CharField(max_length=255)
    street2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.street1, self.street2, self.city, self.state, self.zipcode, self.country)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"


'''
The phone model is just a generic address container
'''


class PhoneModel(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
                                 )
    phone_number = models.CharField(_('Phone Number'), validators=[phone_regex],
                                    max_length=15, blank=True, unique=True
                                    )  # validators should be a list

    def __str__(self):
        return '%s' % (self.phone_number)

    class Meta:
        verbose_name = "Phone Number"
        # verbose_name_plural = "Phone Numbers"


class CompanyModel(models.Model):
    name = models.CharField(_('Company Name'), max_length=255, blank=False)
    website = models.URLField(_('Company Website'), blank=True)
    since = models.DateField(auto_now_add=True)
    rate = models.DecimalField(max_digits=5, decimal_places=2, blank=False)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        ordering = ['name']
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class EquipmentModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        ordering = ['name']
        verbose_name = 'Equipment'


'''
The site model consists of sites of a company as
some companies have several sites that we will work from.
'''


class SiteModel(models.Model):
    company = models.ForeignKey(
        CompanyModel, on_delete=models.PROTECT, related_name='sites')
    address = models.ForeignKey(AddressModel, on_delete=models.PROTECT)
    phone = models.ForeignKey(PhoneModel, blank=True,
                              null=True, on_delete=models.PROTECT)
    distance = models.SmallIntegerField(blank=True)

    def __str__(self):
        return '%s - %s, %s' % (self.company, self.address.city, self.address.state)

    class Meta:
        ordering = ['company']
        verbose_name = 'Company Site Information'
        verbose_name_plural = 'Company Sites'


'''
The contact model consists of contacts of a company that may
will not have user credentials to log into this system.
Basically, it's just simply site contact information.
'''


class ContactModel(models.Model):
    company = models.ForeignKey(
        CompanyModel, on_delete=models.PROTECT, null=True)
    site = models.ForeignKey(
        SiteModel, on_delete=models.PROTECT, blank=True, null=True, related_name='contact')
    first_name = models.CharField(_('First Name'), max_length=255)
    last_name = models.CharField(_('Last Name'), max_length=255)
    email = models.EmailField(_('E-mail Address'), max_length=255, unique=True)
    office_phone = models.ForeignKey(PhoneModel, on_delete=models.PROTECT)
    cell_phone = models.ForeignKey(PhoneModel,
                                   on_delete=models.PROTECT,
                                   blank=True,
                                   null=True,
                                   related_name='c_cell_phone')
    extension = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '%s %s of %s, %s;%s' % (self.first_name, self.last_name, self.company, self.office_phone, self.extension)

    class Meta:
        ordering = ['company']
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
