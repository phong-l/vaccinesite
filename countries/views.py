from django.shortcuts import render
from django.views.generic import ListView
from .models import Country
from django.db.models import Q


class HomePage(ListView):
    model = Country
    template_name = 'home.html'
    context_object_name = 'countries'

    def get_queryset(self):
        country = self.request.GET.get('searchcountry')
        continent = self.request.GET.get('searchcontinent')
        q = self.model.objects.all()
        if country:
            q = Country.objects.filter(Q(name__icontains=country))
        elif continent:
            q = Country.objects.filter(Q(continent__icontains=continent))
        return q
