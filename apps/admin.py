from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline
from django.contrib.auth.admin import UserAdmin

from apps.models import Category, Product, User, ProductPhoto


class ProductPhotoStackedInline(StackedInline):
    model = ProductPhoto
    extra = 1
    min_num = 1


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(Category)
class CategoryModelAdmin(ModelAdmin):
    pass


@admin.register(Product)
class CustomModelAdmin(ModelAdmin):
    inlines = [ProductPhotoStackedInline]
