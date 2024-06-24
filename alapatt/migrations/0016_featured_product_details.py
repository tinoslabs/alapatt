# Generated by Django 5.0.6 on 2024-06-22 08:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alapatt', '0015_featured_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Featured_Product_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=100, null=True)),
                ('product_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('product_image', models.ImageField(upload_to='images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alapatt.new_category')),
            ],
        ),
    ]