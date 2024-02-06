# Generated by Django 5.0.1 on 2024-02-06 19:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('moon_type', models.CharField(choices=[('PR', 'Predominantly Rocky'), ('PI', 'Predominantly Icy')], max_length=3)),
                ('equitorial_diameter', models.DecimalField(decimal_places=4, max_digits=6)),
                ('mass', models.DecimalField(decimal_places=9, max_digits=10)),
                ('semi_major_axis', models.IntegerField()),
                ('orbital_period', models.DecimalField(decimal_places=3, max_digits=5)),
                ('inclination_to_primarys_equator', models.DecimalField(decimal_places=3, max_digits=5)),
                ('orbital_eccentricity', models.DecimalField(decimal_places=4, max_digits=6)),
                ('axial_tilt', models.DecimalField(decimal_places=2, max_digits=3)),
                ('atmosphere', models.CharField(max_length=200)),
                ('planet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.planet')),
            ],
        ),
    ]
