from django.contrib import admin
from .models import Category,Product,Some

# Register your models here.
#Модель категории
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}

#Модель товара
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','slug','price','stock','available','created','updated']
    list_filter=['available','created','updated']
    list_editable=['price','stock','available']
    prepopulated_fields={'slug':('name',)}

class SomeAdmin(admin.ModelAdmin):
    list_display=['slug','name','detail','check']
    list_editable=['name','detail']
    prepopulated_fields={'slug':('name',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Some,SomeAdmin)
#admin.site.disable_action('delete_selected')
