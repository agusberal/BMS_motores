# Generated by Django 4.2.6 on 2024-11-29 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculos',
            fields=[
                ('Codigo', models.AutoField(primary_key=True, serialize=False)),
                ('Modelo', models.TextField(max_length=30)),
                ('Marca', models.TextField(max_length=30)),
                ('Desripcion', models.TextField(max_length=150, null=True)),
                ('Precio', models.IntegerField()),
                ('Cantidad', models.PositiveIntegerField()),
                ('Imagen', models.ImageField(null=True, upload_to='autos')),
            ],
        ),
    ]
