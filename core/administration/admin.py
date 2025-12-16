from django.contrib import admin
from . models import AdminProfile, AdminReport


@admin.register(AdminProfile)
class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'phone')


@admin.register(AdminReport)
class AdminReportAdmin(admin.ModelAdmin):
    list_display = ('admin', 'work_report', 'communication', 'feedback', 'status', 'created_at')
