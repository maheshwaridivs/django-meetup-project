from django.contrib import admin
from web_app.models import *


# to show multiple column list for created record and pass to in register model
# class MeetupAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'location')

#     # filter will be added in admin panel of meetup model
#     # list_filter = ('title',)

#     # it will create slug field automatically based on title field
#     prepopulated_fields = {'slug': ('title',)}

# Register your models here.
# admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Meetup)
admin.site.register(Participant)

