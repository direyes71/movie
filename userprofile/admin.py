from django.contrib import admin

from userprofile.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
    )
    search_fields = (
        'username',
    )


admin.site.register(Profile, ProfileAdmin)
