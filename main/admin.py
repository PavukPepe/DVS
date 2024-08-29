from django.contrib import admin
from .models import *
from django.utils.html import format_html


class EngineAdmin(admin.ModelAdmin):
    list_display = ('name', 'fuel_type', 'volume', 'state_of_origin', 'condition', 'price', 'price_order')
    search_fields = ('name', 'state_of_origin')
    list_filter = ('fuel_type', 'state_of_origin', 'condition')
    list_editable = ('price', 'price_order')
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'photo', 'fuel_type', 'volume', 'state_of_origin', 'condition')
        }),
        ('Цены', {
            'fields': ('price', 'price_order')
        }),
        ('Дополнительно', {
            'fields': ('generations',)
        }),
    )


admin.site.register(Engine, EngineAdmin)


class CarBrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo_preview')
    search_fields = ('name',)
    ordering = ('name',)

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.logo.url)
        return "Нет логотипа"
    logo_preview.short_description = 'Логотип'


admin.site.register(CarBrand, CarBrandAdmin)


class CarGenerationAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'get_brand_name')
    search_fields = ('name', 'model__name', 'model__brand__name')
    list_filter = ('model',)
    ordering = ('model', 'name')

    def get_brand_name(self, obj):
        return obj.model.brand.name

    get_brand_name.short_description = 'Марка'


admin.site.register(CarGeneration, CarGenerationAdmin)


class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand')
    search_fields = ('name', 'brand__name')
    list_filter = ('brand',)
    ordering = ('brand', 'name')
    def brand_name(self, obj):
        return obj.brand.name

    brand_name.short_description = 'Марка'


admin.site.register(CarModel, CarModelAdmin)

@admin.register(OrderEngine)
class OrderEngineAdmin(admin.ModelAdmin):
    list_display = ('engine', 'phone', 'status')  # Поля, которые вы хотите видеть в списке
    search_fields = ('engine', 'phone')            # Поисковые поля
    list_filter = ('status',)                       # Фильтрация по статусу
    ordering = ('-id',)


