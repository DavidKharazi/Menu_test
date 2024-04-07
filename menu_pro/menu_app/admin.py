from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_filter = ('parent',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(MenuItem, MenuItemAdmin)



