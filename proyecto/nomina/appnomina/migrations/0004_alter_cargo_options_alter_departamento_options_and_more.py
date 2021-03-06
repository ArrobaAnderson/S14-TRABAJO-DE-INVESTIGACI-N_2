# Generated by Django 4.0.3 on 2022-03-22 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appnomina', '0003_alter_cargo_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cargo',
            options={'ordering': ['id'], 'verbose_name': 'Cargo', 'verbose_name_plural': 'Cargos'},
        ),
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['id'], 'verbose_name': 'Departamento', 'verbose_name_plural': 'Departamentos'},
        ),
        migrations.AlterField(
            model_name='departamento',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
