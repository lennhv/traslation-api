from django.contrib import admin

# Register your models here.

from .models import Traslation


site = admin.site


class TraslationAdmin(admin.ModelAdmin):
    list_display = ('id', 'lang_source', 'lang_target',
                    'status', 'creation_time', 'finish_time')


admin.site.register(Traslation, TraslationAdmin)
