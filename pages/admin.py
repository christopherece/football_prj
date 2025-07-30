from django.contrib import admin
from django.utils.html import format_html
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

# @admin.register(TrainingPhoto)
# class TrainingPhotoAdmin(admin.ModelAdmin):
#     list_display = ('title', 'display_image', 'is_active', 'created_at')
#     list_filter = ('is_active', 'created_at')
#     search_fields = ('title',)
#     list_editable = ('is_active',)
#     readonly_fields = ('created_at',)
#     date_hierarchy = 'created_at'
#     ordering = ('-created_at',)
    
#     def display_image(self, obj):
#         if obj.image:
#             return format_html(
#                 '<img src="{}" style="max-height: 100px; max-width: 150px;" />',
#                 obj.image.url
#             )
#         return "No Image"
#     display_image.short_description = 'Preview'
