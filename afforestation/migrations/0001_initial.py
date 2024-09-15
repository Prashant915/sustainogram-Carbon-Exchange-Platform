# Generated by Django 5.0.6 on 2024-07-10 10:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Planted_trees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project_Name', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=100)),
                ('Date_of_Plantation', models.DateField()),
                ('Species_Planted', models.CharField(max_length=100)),
                ('Area_Planted', models.IntegerField()),
                ('Number_of_Trees_Planted', models.IntegerField()),
                ('Planting_Density', models.IntegerField()),
                ('Action', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trees_Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Species_Planted', models.CharField(max_length=100)),
                ('Growth_Rate_Height', models.FloatField()),
                ('Growth_Rate_Diameter', models.IntegerField()),
                ('Survival_Rate', models.IntegerField()),
                ('Above_Ground_Biomass', models.IntegerField()),
                ('Below_Ground_Biomass', models.IntegerField()),
                ('Action', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
