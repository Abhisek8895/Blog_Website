from django.contrib import admin
from . models import Category, Blog
# Register your models here.

class CatgoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'created_at', 'updated_at')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'auther', 'status', 'is_feachered', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    search_field = ('id', 'title', 'category', 'status')
    list_editable = ('is_feachered','status',)

admin.site.register(Category, CatgoryAdmin)
admin.site.register(Blog, BlogAdmin)