# Generated by Django 4.0.3 on 2022-03-24 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appnomina', '0007_alter_departamento_descripcion_alter_empleado_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='nombre',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
