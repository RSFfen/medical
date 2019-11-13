from django.contrib import admin

from .models import Client
from .models import Firm
from .models import OKVED

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth', 'firm', 'experience', 'prof', 'rec_created')
    list_display_links = ('name', )
    search_fields = ('name', )

admin.site.register(Client, ClientAdmin)

class FirmAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_ownership', 'type_econom_activity',  'rec_created')
    list_display_links = ('name', )
    search_fields = ('name', )

admin.site.register(Firm, FirmAdmin)

class OKVEDAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'section',  'subsection')
    list_display_links = ('code', )
    search_fields = ('code', )

admin.site.register(OKVED, OKVEDAdmin)
