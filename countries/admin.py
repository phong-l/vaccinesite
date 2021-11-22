from django.contrib import admin
from .models import Country


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'continent', 'required')


admin.site.register(Country, CountryAdmin)
