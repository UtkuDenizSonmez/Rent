from django.contrib import admin
from .models import Car, Offer, Header, CarImageTable


class CarImageInline(admin.TabularInline):
    model = CarImageTable


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    inlines = [
        CarImageInline
    ]
    prepopulated_fields = {"slug": ("brand", )}


class OfferAdmin(admin.ModelAdmin):
    list_display = ["title", "subtitle", "description", "is_active", "created_at"]
    list_filter = ["is_active"]


class HeaderAdmin(admin.ModelAdmin):
    list_display = ["title", "default", "created_at"]


admin.site.register(Offer, OfferAdmin)
admin.site.register(Header, HeaderAdmin)





