# Generated by Django 2.2.6 on 2019-10-23 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20191022_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image5',
            field=models.ImageField(blank=True, default='packaging.jpg', null=True, upload_to='product_images'),
        ),
    ]