# Generated by Django 4.1.1 on 2022-11-04 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libreria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('genero', models.CharField(max_length=30)),
                ('mes_venta', models.DateField()),
            ],
        ),
    ]
