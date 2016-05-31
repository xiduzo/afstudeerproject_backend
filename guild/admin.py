from django.contrib import admin

from guild.models import Guild, UserInGuild

# Register your models here.
admin.site.register(Guild)
admin.site.register(UserInGuild)
