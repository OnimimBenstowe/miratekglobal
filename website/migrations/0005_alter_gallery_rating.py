# Generated by Django 4.2.6 on 2024-05-18 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_gallery_price_gallery_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='rating',
            field=models.CharField(choices=[('premium', 'premium'), ('standard', 'standard'), ('deluxe', 'deluxe')], default='rating', max_length=10, null=True),
        ),
    ]