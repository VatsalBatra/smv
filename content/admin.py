from django.contrib import admin
from .models import image_slide,our_ride,crew_sir,crew_members,partners,achievement

@admin.register(image_slide)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['caption','image_tag']
@admin.register(our_ride)
class ProductsAdmin_ourride(admin.ModelAdmin):
    list_display = ['title','image_tag']

    
@admin.register(crew_sir)
@admin.register(crew_members)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(achievement)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title','image_tag']

@admin.register(partners)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name','image_tag']



# Register your models here.
