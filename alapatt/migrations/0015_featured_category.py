# Generated by Django 5.0.6 on 2024-06-22 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alapatt', '0014_alter_contactmodel_comment_alter_contactmodel_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Featured_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('status', models.BooleanField(default=False, help_text='0-default,1-Hidden')),
            ],
        ),
    ]