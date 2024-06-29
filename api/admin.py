from django.contrib import admin

from .models import *

admin.site.register(Customer)
admin.site.register(Manager)
admin.site.register(RealEstate)
admin.site.register(RealEstateDetails)
admin.site.register(Seller)