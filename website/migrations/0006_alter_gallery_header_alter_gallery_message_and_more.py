# Generated by Django 4.2.6 on 2024-05-18 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_gallery_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='header',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='message',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]