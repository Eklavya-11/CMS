from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')

admin.site.site_header = "CMS Admin Panel"
# loop hole: if user isn't admin how will they login using admin panel? not a major issue but works.
