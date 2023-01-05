from django.contrib import admin
from .models import Event, EventsHistory, Months, Image
from .models import HoursResult


class HoursResultAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'hours', 
        'minutes',
        'visits',
        'publications',
        'films',
        )


class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'name', 
        'image',
        )

admin.site.register(Event)
admin.site.register(EventsHistory)
admin.site.register(HoursResult, HoursResultAdmin)
admin.site.register(Months)
admin.site.register(Image, ImageAdmin)
