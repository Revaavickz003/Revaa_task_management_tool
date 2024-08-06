# Generated by Django 5.0.4 on 2024-08-06 13:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_events_weekday'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='all_team',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='frontend.team'),
        ),
    ]
