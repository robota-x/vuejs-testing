from django.contrib import admin

from . import models


@admin.register(models.EnquiryType)
class EnquiryTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Office)
class OfficeAdmin(admin.ModelAdmin):
    pass