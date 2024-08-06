# Generated by Django 5.0.4 on 2024-08-06 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_remove_events_all_sunday_alter_events_all_friday_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='end_time',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='satrt_time',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='start_date',
            field=models.DateField(),
        ),
    ]
