# Generated by Django 3.2.18 on 2023-03-14 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_collection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='image',
            field=models.ImageField(upload_to='Product_image'),
        ),
    ]
