# Generated by Django 5.0.4 on 2024-08-06 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='typeOfEvent',
            field=models.CharField(blank=True, choices=[('None', 'Project'), ('Gray', 'Call'), ('Blue', 'Event'), ('Green', 'Meeting')], max_length=10, null=True),
        ),
    ]
