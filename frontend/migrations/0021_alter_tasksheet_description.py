# Generated by Django 5.0.4 on 2024-06-15 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0020_alter_tasksheet_eta_alter_tasksheet_end_date_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasksheet',
            name='description',
            field=models.TextField(),
        ),
    ]