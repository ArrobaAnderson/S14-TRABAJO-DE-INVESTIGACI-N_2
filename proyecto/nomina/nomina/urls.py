from django.contrib import admin
from django.urls import path
from appnomina.views import inicio, cargo, crearCargo,editarCargo,eliminarCargo,departamento,crearDepartamento,editarDepartamento,eliminarDepartamento,empleado,crearEmpleado,editarEmpleado,eliminarEmpleado
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio,name="inicio" ),
    #referencio la vista crearCargo al momento (cargo/)
    path('cargo/',cargo,name="cargo" ),
    path('crear_cargo/',crearCargo,name="crear_cargo" ),
    path('editar_cargo/<int:id>', editarCargo, name="editar_cargo"),
    path('eliminar_cargo/<int:id>', eliminarCargo, name='eliminar_cargo'),
    path('departamento/',departamento,name="departamento" ),
    path('crear_departamento/',crearDepartamento,name="crear_departamento" ),
    path('editar_departamento/<int:id>', editarDepartamento, name="editar_departamento"),
    path('eliminar_departamento/<int:id>', eliminarDepartamento, name='eliminar_departamento'),
    path('empleado/',empleado,name="empleado" ),
    path('crear_empleado/',crearEmpleado,name="crear_empleado" ),
    path('editar_empleado/<int:id>',editarEmpleado,name="editar_empleado" ),
    path('eliminar_empleado/<int:id>',eliminarEmpleado,name="eliminar_empleado" ),
]
