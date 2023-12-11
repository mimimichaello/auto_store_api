from django.contrib import admin
from users.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'date_of_registration',)
    list_display_links = ('username',)
    list_filter = ('username',)
    fields = ('first_name', 'last_name', 'email',)


admin.site.register(User, UserAdmin)
