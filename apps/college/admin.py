from django.contrib import admin
from apps.college.models import CollegeBranch


class CollegeBranchAdmin(admin.ModelAdmin):
    """Admin interface to manage coupon types."""

    list_display = ('id', 'branch_name')
    list_filter = ('branch_name',)
    search_fields = ('branch_name',)

admin.site.register(CollegeBranch, CollegeBranchAdmin)
