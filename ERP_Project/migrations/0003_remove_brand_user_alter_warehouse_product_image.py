# Generated by Django 5.0.4 on 2024-04-25 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERP_Project', '0002_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='user',
        ),
        migrations.AlterField(
            model_name='warehouse_product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
