# Generated by Django 2.2.5 on 2019-10-03 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20191002_2025'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Product Category', 'verbose_name_plural': 'Products Category'},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name': 'Image', 'verbose_name_plural': 'Images'},
        ),
    ]
