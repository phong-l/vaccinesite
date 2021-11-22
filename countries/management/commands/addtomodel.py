from django.core.management.base import BaseCommand
import pandas as pd
from countries.models import Country


class Command(BaseCommand):

    help = 'Import countries'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        df = pd.read_csv('countries.csv')
        for name, continent, required in zip(df.country, df.continent, df.required):
            models = Country(name=name, continent=continent, required=required)
            models.save()
