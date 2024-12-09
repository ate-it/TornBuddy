# Register your models here.
from django.contrib import admin

from .models import Faction, FactionMember

admin.site.register(Faction)
admin.site.register(FactionMember)
