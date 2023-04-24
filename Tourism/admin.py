from django.contrib import admin
from .models import Touristik_hudular, Category, Contact, Viloyatlar


# Register your models here.

@admin.register(Touristik_hudular)
class AdminSahifa(admin.ModelAdmin):
    list_display = ['Mavzu', 'slug', 'category', 'yozilgan_vaqti', 'yaratilgan_vaqti', 'yangilangan_vaqti', 'status']
    list_filter = ['category', 'yaratilgan_vaqti', 'status']
    prepopulated_fields = {"slug":('Mavzu',)}
    date_hierarchy = 'yozilgan_vaqti'
    search_fields = ['Mavzu', 'Matn', 'category']
    ordering = ['status', 'yozilgan_vaqti']

# @admin.register(Viloyatlar)
# class AdminViloyat(admin.ModelAdmin):
#     list_display = ['hudud']


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['Nomi']

@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ['ism', 'email']
