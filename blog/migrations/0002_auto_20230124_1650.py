# Generated by Django 3.2.16 on 2023-01-24 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='post_image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
