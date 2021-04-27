from django.contrib import admin
from . import models


@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'status', 'main_post', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',), }


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'developer', 'last_version', 'website', 'slug')
    prepopulated_fields = {'slug': ('name',), }


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
