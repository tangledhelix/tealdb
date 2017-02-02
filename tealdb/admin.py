from django.contrib import admin

from .models import Site, SiteAdmin
from .models import Contact, ContactAdmin

admin.site.register(Site, SiteAdmin)
admin.site.register(Contact, ContactAdmin)
