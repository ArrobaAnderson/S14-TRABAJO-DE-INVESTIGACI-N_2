from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib import admin
from django import forms
from .models import Cargo, Departamento, Empleado

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['descripcion','activo']
        widgets = {
            'descripcion':forms.TextInput(attrs={
                'placeholder':'Ingrese cargo',
                'class':'form-group',
                'required':True
            }),
        }

class DepartamentoForm(forms.ModelForm):
    class Meta:  
        model = Departamento
        fields = ['descripcion','activo']
        widgets = {
            'descripcion':forms.TextInput(attrs={
                'placeholder':'Ingrese departamento',
                'class':'form-group',
                'required':True
            }),
        }
        
class EmpleadoForm(forms.ModelForm):
    class Meta:  
        model = Empleado
        fields = ['id','nombre','cedula','cargo','departamento','sueldo','activo']
        widgets = {
            'nombre':forms.TextInput(attrs={
                'placeholder':'Ingrese Nombre',
                'class':'form-group',
                'required':True
            }),
            'cedula':forms.TextInput(attrs={
                'placeholder':'Ingrese Cedula',
                'class':'form-group',
                'type':"number",
                'required':True
            }),
            'sueldo':forms.TextInput(attrs={
                'placeholder':'Ingrese Sueldo',
                'class':'form-group',
                'type':'number',
                'required':True
            }),
        }