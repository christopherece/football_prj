from django.contrib import admin
from django.utils.html import format_html
from .models import Gallery

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'title', 'category', 'created_at')
    list_display_links = ('title',)
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    list_per_page = 20
    
    def thumbnail(self, obj):
        return format_html('<img src="{}" width="50" height="50" style="object-fit: contain;" />', obj.image.url if obj.image else '')
    thumbnail.short_description = 'Image'

    fieldsets = (
        ('Gallery Item', {
            'fields': ('title', 'description', 'image', 'category')
        }),
    )

    class Media:
        css = {
            'all': ('admin/css/custom.css',)
        }
        js = ('admin/js/custom.js',)
