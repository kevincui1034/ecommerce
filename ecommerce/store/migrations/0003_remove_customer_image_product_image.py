# Generated by Django 4.0.4 on 2022-05-13 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_customer_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
