from django.contrib import admin
from inventario.models import venta
# Register your models here.
class VentasAdmin(admin.ModelAdmin):
    list_display = ["mes","cantidad","barrio"]


admin.site.register(venta, VentasAdmin)
