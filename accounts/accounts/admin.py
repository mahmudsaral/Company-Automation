from django.contrib import admin
from .models import *
from accounts.models import Event, EventMember
from django.forms import ModelForm, DateInput

class EventMemberAdmin(admin.ModelAdmin):
    model = EventMember
    list_display = ['event', 'Personel_Adı']

admin.site.register(firma)
admin.site.register(Order)
admin.site.register(fbf)
admin.site.register(Event)
admin.site.register(EventMember, EventMemberAdmin)
admin.site.register(Denetci_9001)
admin.site.register(kontrol)
