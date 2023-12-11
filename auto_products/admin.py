from django.contrib import admin
from auto_products.models import Car, Accessory, Category, Basket

class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'model')
    list_display_links = ('name',)
    list_filter = ('name', 'model', 'release', 'body')
    fields = ('name', 'model', 'release', 'body', 'color', 'price', 'category', 'creator')

admin.site.register(Car, CarAdmin)
admin.site.register(Accessory)
admin.site.register(Category)
admin.site.register(Basket)
