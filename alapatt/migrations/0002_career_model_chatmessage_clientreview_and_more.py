# Generated by Django 5.0.6 on 2024-07-12 05:40

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alapatt', '0001_initial'),
    ]

    operations = [
        # migrations.CreateModel(
        #     name='Career_Model',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('job_position', models.CharField(max_length=100)),
        #         ('job_type', models.CharField(max_length=100)),
        #         ('company_name', models.CharField(max_length=100)),
        #         ('place', models.CharField(max_length=100)),
        #         ('salary', models.IntegerField()),
        #         ('job_details', ckeditor.fields.RichTextField(max_length=20000)),
        #         ('posted_date', models.DateField()),
        #         ('end_date', models.DateTimeField()),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='ChatMessage',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('name', models.CharField(max_length=100)),
        #         ('phone_number', models.CharField(max_length=15)),
        #         ('email', models.EmailField(max_length=254)),
        #         ('message', models.TextField()),
        #         ('created_at', models.DateTimeField(auto_now_add=True)),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='ClientReview',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('client_name', models.CharField(blank=True, max_length=100, null=True)),
        #         ('client_image', models.ImageField(blank=True, null=True, upload_to='client_images/')),
        #         ('review', models.TextField(blank=True, null=True)),
        #         ('review_video', models.FileField(blank=True, null=True, upload_to='review_videos/')),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='collections_category',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('collection_name', models.CharField(max_length=100)),
        #         ('status', models.BooleanField(default=False, help_text='0-default,1-Hidden')),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='ContactModel',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('name', models.CharField(max_length=100)),
        #         ('phone', models.CharField(blank=True, max_length=20, null=True)),
        #         ('email', models.EmailField(blank=True, max_length=254, null=True)),
        #         ('subject', models.CharField(blank=True, max_length=200, null=True)),
        #         ('comment', models.TextField(blank=True, null=True)),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='Featured_Category',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('category_name', models.CharField(max_length=100)),
        #         ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
        #         ('description', models.CharField(blank=True, max_length=500, null=True)),
        #         ('status', models.BooleanField(default=False, help_text='0-default,1-Hidden')),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='GoldRate',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('gold_rate', models.DecimalField(decimal_places=2, max_digits=8)),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='New_Category',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('category_name', models.CharField(max_length=100)),
        #         ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
        #         ('description', models.CharField(blank=True, max_length=500, null=True)),
        #         ('status', models.BooleanField(default=False, help_text='0-default,1-Hidden')),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='test_category',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('collection_name', models.CharField(max_length=100)),
        #         ('collection_slug', models.SlugField(blank=True, max_length=100, unique=True)),
        #         ('status', models.BooleanField(default=False, help_text='0-default,1-Hidden')),
        #     ],
        # ),
        # migrations.AlterField(
        #     model_name='enquirymodel',
        #     name='comment',
        #     field=models.TextField(max_length=1000),
        # ),
        # migrations.CreateModel(
        #     name='Featured_Products',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('product_name', models.CharField(blank=True, max_length=100, null=True)),
        #         ('product_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
        #         ('product_image', models.ImageField(upload_to='images/')),
        #         ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alapatt.featured_category')),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='Job_Application',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('first_name', models.CharField(max_length=100)),
        #         ('last_name', models.CharField(max_length=100)),
        #         ('address', models.CharField(max_length=500)),
        #         ('email', models.EmailField(blank=True, max_length=100, null=True)),
        #         ('phone', models.CharField(blank=True, max_length=20, null=True)),
        #         ('pdf_file', models.FileField(upload_to='pdfs/')),
        #         ('job_position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidates', to='alapatt.career_model')),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='Product_Details',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('product_name', models.CharField(blank=True, max_length=100, null=True)),
        #         ('product_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
        #         ('product_image', models.ImageField(upload_to='images/')),
        #         ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alapatt.new_category')),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='sub_category',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('product_name', models.CharField(blank=True, max_length=100, null=True)),
        #         ('status', models.BooleanField(default=False, help_text='0-default,1-Hidden')),
        #         ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alapatt.collections_category')),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='Collections_Details',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('name', models.CharField(blank=True, max_length=100, null=True)),
        #         ('product_image', models.ImageField(upload_to='collections_images/')),
        #         ('product_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
        #         ('status', models.BooleanField(default=False, help_text='0-default,1-Hidden')),
        #         ('collections', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alapatt.collections_category')),
        #         ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alapatt.sub_category')),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='sub_test',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('product_name', models.CharField(blank=True, max_length=100, null=True)),
        #         ('product_slug', models.SlugField(blank=True, max_length=100, unique=True)),
        #         ('status', models.BooleanField(default=False, help_text='0-default,1-Hidden')),
        #         ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alapatt.collections_category')),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='test_Details',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('name', models.CharField(blank=True, max_length=100, null=True)),
        #         ('product_image', models.ImageField(upload_to='collections_images/')),
        #         ('product_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
        #         ('status', models.BooleanField(default=False, help_text='0-default,1-Hidden')),
        #         ('collections', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alapatt.collections_category')),
        #         ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alapatt.sub_category')),
        #     ],
        # ),
    ]
