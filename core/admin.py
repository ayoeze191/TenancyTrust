from django.contrib import admin
from .models import Property, TenantProfile, Agreement
# Register your models here.
admin.site.register(Property)
admin.site.register(TenantProfile)
admin.site.register(Agreement)

