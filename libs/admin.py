from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from .models import (
    Company,
    User,
)
from game.admin import ScoreInlineAdmin
from libs.admin_helpers import CompanySpecificMixin


class MyUserAdmin(CompanySpecificMixin, UserAdmin):
    list_display = ('username', 'display_teams', 'is_staff')
    inlines = (ScoreInlineAdmin,)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    search_fields = ('username', 'first_name', 'last_name', 'email', 'avatar__name')

    def display_teams(self, obj):
        team = obj.teams.first()
        if team:
            return team.name
        return ''

    display_teams.admin_order_field = 'teams'

    def get_fieldsets(self, request, obj=None):
        if request.user.is_superuser:
            if not obj:
                return self.add_fieldsets
            return ((None, {'fields': ('username', 'password', 'company')}),
                    (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
                    (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                                   'groups', 'user_permissions')}),
                    (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
                    )

        return super(MyUserAdmin, self).get_fieldsets(request, obj)


admin.site.register(Company)
# admin.site.register(User, MyUserAdmin)
