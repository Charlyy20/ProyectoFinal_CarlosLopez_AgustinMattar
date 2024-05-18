from django.contrib import admin
from . import models

admin.site.site_title = 'Tienda de Accesorios'

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'precio')
    list_display_links = ('marca',) 

admin.site.register(models.Llantas, ProductsAdmin)
admin.site.register(models.Alerones, ProductsAdmin)
admin.site.register(models.Spoilers, ProductsAdmin)
admin.site.register(models.Intakes, ProductsAdmin)
admin.site.register(models.Widebody, ProductsAdmin)