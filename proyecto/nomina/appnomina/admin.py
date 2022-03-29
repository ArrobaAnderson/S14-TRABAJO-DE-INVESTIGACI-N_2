from re import search
from django.contrib import admin
from .models import Cargo, Empleado, Departamento
# añadimmos los modelos (mantenimientos o formularios) al administrador
        
admin.site.register(Cargo)
admin.site.register(Departamento)
admin.site.register(Empleado)
