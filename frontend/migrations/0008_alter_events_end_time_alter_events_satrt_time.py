# Generated by Django 5.0.4 on 2024-08-06 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0007_events_end_time_events_satrt_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='satrt_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]