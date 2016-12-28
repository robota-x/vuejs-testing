from django.db import models
from django.utils.text import Truncator


class EnquiryType(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return '{0}: {1}'.format(self.name, Truncator(self.description).chars(70))


class Enquiry(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    email = models.EmailField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    other_contact = models.TextField(blank=True, null=True)

    text = models.TextField()
    type = models.ForeignKey(EnquiryType)

    def __str__(self):
        return '{0} {1}: {2}'.format(self.first_name, self.last_name, Truncator(self.text).chars(70))
