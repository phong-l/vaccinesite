from django.db import models


class Country(models.Model):
    ASIA = 'ASIA'
    SOUTH_AMERICA = 'SOUTH AMERICA'
    NORTH_AMERICA = 'NORTH AMERICA'
    EUROPE = 'EUROPE'
    AFRICA = 'AFRICA'
    OCEANIA = 'OCEANIA'
    ANTARCTICA = 'ANTARCTICA'
    CONTINENT_CHOICES = [
        (ASIA, 'Asia'),
        (SOUTH_AMERICA, 'South America'),
        (NORTH_AMERICA, 'North America'),
        (EUROPE, 'Europe'),
        (AFRICA, 'Africa'),
        (OCEANIA, 'Oceania'),
        (ANTARCTICA, 'Antarctica')
    ]
    DOUBLE = 'DV'
    SINGLE = 'SV'
    NONE = 'No'
    UNKNOWN = 'NA'
    REQUIRED_CHOICES = [
        (DOUBLE, 'Double'),
        (SINGLE, 'Single'),
        (NONE, 'No'),
        (UNKNOWN, 'Unknown'),
    ]
    name = models.TextField(max_length=255)
    continent = models.CharField(max_length=20, choices=CONTINENT_CHOICES)
    required = models.CharField(max_length=20, choices=REQUIRED_CHOICES)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name