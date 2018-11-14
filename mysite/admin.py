from django.contrib import admin
from .models import Work, Official_Bio, Nodanews_Description, Agency, Meeting


class MeetingAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'date', 'agency']


admin.site.register(Work)
admin.site.register(Official_Bio)
admin.site.register(Nodanews_Description)
admin.site.register(Agency)
admin.site.register(Meeting, MeetingAdmin)
# Register your models here.
