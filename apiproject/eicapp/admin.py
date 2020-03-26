from django.contrib import admin
from eicapp.models import Sector, NewsEvent, Incentive, CountryProfile, Service, ChinesePage, Email

admin.site.register(Sector)
admin.site.register(NewsEvent)
admin.site.register(Incentive)
admin.site.register(CountryProfile)
admin.site.register(Service)
admin.site.register(ChinesePage)
admin.site.register(Email)

admin.site.site_header = "EIC ADMIN ONLY"