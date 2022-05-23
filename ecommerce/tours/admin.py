from django.contrib import admin

# Register your models here.
from .models import Cliente,Region,Tour,Compra

admin.site.register(Cliente)
admin.site.register(Region)
admin.site.register(Tour)
admin.site.register(Compra)