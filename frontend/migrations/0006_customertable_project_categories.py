# Generated by Django 5.0.4 on 2024-06-05 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_remove_customertable_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customertable',
            name='project_categories',
            field=models.CharField(choices=[('Creative', 'Creative'), ('Digital Marketing', 'Digital Marketing'), ('Development', 'Development'), ('Client Relationship', 'Client Relationship')], default=None, max_length=19),
            preserve_default=False,
        ),
    ]