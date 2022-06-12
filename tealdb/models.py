import datetime

from django.db import models
from django.contrib import admin


class Site(models.Model):
    name = models.CharField(max_length=128, default='')
    address1 = models.CharField(max_length=128, default='')
    address2 = models.CharField(max_length=128, default='')
    city = models.CharField(max_length=64, default='')
    state = models.CharField(max_length=32, default='')
    postal_code = models.CharField(max_length=32, default='')
    country = models.CharField(max_length=64, default='')
    web_site = models.URLField(default='')
    email = models.EmailField(default='')
    phone = models.CharField(max_length=32, default='')
    fax = models.CharField(max_length=32, default='')
    have_lit = models.BooleanField(default=False)
    years_lit = models.CharField(max_length=128, default='')
    map_link = models.URLField(max_length=512, default='')
    fee = models.BooleanField(default=False)
    notes = models.TextField(default='')
    submission_date = models.TextField(default='')
    lighting_start_date = models.TextField(default='')
    lighting_end_date = models.TextField(default='')
    applied_this_year = models.BooleanField(default=False)
    accepted_this_year = models.BooleanField(default=False)
    lightings_not_available = models.BooleanField(default=False)
    action_required = models.BooleanField(default=False)
    twitter = models.CharField(max_length=64, default='')

    NOT_CONTACTED = 'not_contacted'
    PENDING = 'pending'
    RESPONSE_LIT = 'responded_lit'
    RESPONSE_DECLINED = 'responded_declined'
    NO_RESPONSE = 'no_response'
    CONTACT_FAILED = 'contact_failed'

    DISPOSITION_CHOICES = (
        (NOT_CONTACTED, 'Have not contacted yet'),
        (PENDING, 'Contacted, awaiting a response'),
        (RESPONSE_LIT, 'Responded, and site was lit'),
        (RESPONSE_DECLINED, 'Responded, but declined to light'),
        (NO_RESPONSE, 'No response'),
        (CONTACT_FAILED, 'Unable to contact (email bounced, etc.)'),
    )

    disposition = models.CharField(
        max_length=32,
        choices=DISPOSITION_CHOICES,
        default=NOT_CONTACTED,
    )


class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state')


class Contact(models.Model):
    site = models.ForeignKey(Site, default=None, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32, default='')
    last_name = models.CharField(max_length=32, default='')
    address1 = models.CharField(max_length=128, default='')
    address2 = models.CharField(max_length=128, default='')
    city = models.CharField(max_length=64, default='')
    state = models.CharField(max_length=32, default='')
    postal_code = models.CharField(max_length=32, default='')
    country = models.CharField(max_length=64, default='')
    phone = models.CharField(max_length=32, default='')
    fax = models.CharField(max_length=32, default='')
    mobile_phone = models.CharField(max_length=32, default='')
    email = models.EmailField(default='')
    social_twitter = models.CharField(max_length=64, default='')
    social_facebook = models.CharField(max_length=64, default='')
    social_instagram = models.CharField(max_length=64, default='')
    asshole = models.BooleanField(default=False)
    official = models.BooleanField(default=False)
    notes = models.TextField(default='')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

