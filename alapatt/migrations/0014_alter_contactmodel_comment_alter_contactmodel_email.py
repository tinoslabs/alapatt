# Generated by Django 5.0.6 on 2024-06-17 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alapatt', '0013_alter_contactmodel_comment_alter_contactmodel_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
