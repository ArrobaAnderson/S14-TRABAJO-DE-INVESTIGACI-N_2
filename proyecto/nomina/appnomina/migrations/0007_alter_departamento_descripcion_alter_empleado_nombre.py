# Generated by Django 4.0.3 on 2022-03-23 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appnomina', '0006_empleado_cedula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='descripcion',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='nombre',
            field=models.CharField(max_length=100, null=True),
        ),
    ]