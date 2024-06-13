# Generated by Django 5.0.4 on 2024-06-13 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0014_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='color',
            field=models.CharField(blank=True, choices=[('Light', 'None'), ('Medium', 'Gray'), ('Blue', 'Blue'), ('Green', 'Green'), ('Yellow', 'Yellow'), ('Orange', 'Orange'), ('Red', 'Red'), ('Pink', 'Pink'), ('Purple', 'Purple')], max_length=16, null=True),
        ),
    ]