# Generated by Django 5.1 on 2024-08-27 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('darmanara', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='feature_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
    ]
