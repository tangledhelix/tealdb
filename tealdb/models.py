from django.db import models


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


class Contact(models.Model):
    pass

    # first name
    # last name
    # foreign key: site (optional?)
    # street addr 1
    # street addr 2
    # city
    # state/province
    # postal code
    # country
    # telephone
    # fax
    # mobile
    # email
    # twitter
    # facebook
    # instagram
    # asshole?
    # notes
