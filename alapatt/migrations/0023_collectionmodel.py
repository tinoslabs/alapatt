# Generated by Django 5.0.6 on 2024-07-21 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alapatt', '0022_alter_career_model_job_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_type', models.CharField(choices=[('Gold', 'Gold'), ('Diamond', 'Diamond'), ('Precious Stone', 'Precious Stone')], default='Gold', max_length=50)),
            ],
        ),
    ]
