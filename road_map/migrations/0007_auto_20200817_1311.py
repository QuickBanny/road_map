# Generated by Django 3.1 on 2020-08-17 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('road_map', '0006_auto_20200817_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainblock',
            name='quest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocks', to='road_map.mainquest'),
        ),
    ]
