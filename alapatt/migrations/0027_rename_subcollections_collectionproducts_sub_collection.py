# Generated by Django 5.0.6 on 2024-07-21 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alapatt', '0026_aboutvideo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collectionproducts',
            old_name='SubCollections',
            new_name='sub_collection',
        ),
    ]