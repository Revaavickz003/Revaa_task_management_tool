# Generated by Django 5.0.4 on 2024-06-25 10:46

import django.db.models.deletion
import frontend.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField()),
                ('comments_img', models.ImageField(blank=True, null=True, upload_to=frontend.models.comments_image_upload_to)),
                ('corrent_date_time', models.DateTimeField(auto_now_add=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.tasksheet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.employeedetail')),
            ],
        ),
    ]
