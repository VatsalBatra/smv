from django.contrib import admin
from .models import image_slide,our_ride,crew_sir,crew_members,partners,achievement

@admin.register(image_slide)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['caption']
@admin.register(our_ride)
@admin.register(crew_sir)
@admin.register(crew_members)

@admin.register(achievement)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(partners)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name']



# Register your models here.
