# Generated by Django 5.0.6 on 2024-07-21 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alapatt', '0025_collectionproducts'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_link', models.URLField(blank=True, null=True, unique=True)),
            ],
        ),
    ]