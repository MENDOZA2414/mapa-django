# Generated by Django 4.2.7 on 2023-12-03 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_alter_albergue_estado_alter_crucearroyo_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albergue',
            name='estado',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Desactivado', 'Desactivado')], default='Desactivado', max_length=20),
        ),
        migrations.AlterField(
            model_name='albergue',
            name='suministro_electrico',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Desactivado', 'Desactivado')], default='Desactivado', max_length=20),
        ),
        migrations.AlterField(
            model_name='bombero',
            name='suministro_electrico',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Desactivado', 'Desactivado')], default='Desactivado', max_length=20),
        ),
        migrations.AlterField(
            model_name='crucearroyo',
            name='estado',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Desactivado', 'Desactivado')], default='Desactivado', max_length=20),
        ),
        migrations.AlterField(
            model_name='crucearroyo',
            name='suministro_electrico',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Desactivado', 'Desactivado')], default='Desactivado', max_length=20),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='estado',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Desactivado', 'Desactivado')], default='Desactivado', max_length=20),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='estado',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Desactivado', 'Desactivado')], default='Desactivado', max_length=20),
        ),
    ]
