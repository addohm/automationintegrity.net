from django.contrib import admin
from . import models

admin.site.register(models.CompanyModel)
admin.site.register(models.ContactModel)
admin.site.register(models.SiteModel)
admin.site.register(models.AddressModel)
admin.site.register(models.PhoneModel)
admin.site.register(models.EquipmentModel)
# #from .models import PersonModel

# class PersonModelAdmin(admin.ModelAdmin):
#     fieldsets = ((None, {'fields': ['firstName', 'lastName', 'company',
#                                     'phone', 'email']}),)
#     class Meta:
#          verbose_name = 'Person'
#          verbose_name_plural = 'Persons'

# admin.site.register(PersonModel, PersonModelAdmin)