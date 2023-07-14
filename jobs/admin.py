from django.contrib import admin
from .models import Roles, Category

# Register your models here.


class RolesAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'salary',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Roles, RolesAdmin)
admin.site.register(Category, CategoryAdmin)
