# Generated by Django 5.1.3 on 2024-11-08 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_brand_alter_car_brand'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='year',
            new_name='model_year',
        ),
        migrations.AddField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='cars/'),
        ),
        migrations.AddField(
            model_name='car',
            name='plate',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]