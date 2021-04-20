import django_filters
from .models import *


class SnippetFilter(django_filters.FilterSet):

    class Meta:
        model = Denetci_9001
        fields = '__all__'