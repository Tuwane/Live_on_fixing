from django.contrib import admin
from . models import Guard, Sites
# Register your models here.

admin.site.site_header = "GOITSIKHOSI ADMIN PANEL"
admin.site.site_title = "GOITSIKHOSI CONTROL CENTER"
admin.site.index_title = "Welcome to GOITSIKHOSI Management System"


@admin.register(Guard)
class GuarAdmin(admin.ModelAdmin):
    list_display  = ('first_name', 'last_name', 'phone', 'is_active', 'site_location' )
    filter_horizontal = ('sites',)
    
    def site_location(self, obj):
        return ", ".join(
            site.location for site in obj.sites.all()
        )
    site_location.short_description = "Site Locations"
    
@admin.register(Sites)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')