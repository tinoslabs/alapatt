from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
# Create your models here.

class EnquiryModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    subject = models.CharField(max_length=200, null=True, blank=True)
    comment = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class product_category(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False,help_text="0-default,1-Hidden")

    def __str__(self):
        return self.name


class ChatMessage(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
    
    
class ClientReview(models.Model):
    client_name = models.CharField(max_length=100, null=True, blank=True)
    client_image = models.ImageField(upload_to='client_images/', null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    review_video = models.FileField(upload_to='review_videos/', null=True, blank=True)
    def __str__(self):
        return self.client_name


class GoldRate(models.Model):
    gold_rate = models.DecimalField(max_digits=8, decimal_places=2)
    

class New_Category(models.Model):
    category_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True,blank=True)
    description = models.CharField(max_length=500, null=True,blank=True)
    status = models.BooleanField(default=False,help_text="0-default,1-Hidden")

    def __str__(self):
        return self.category_name
    
class Product_Details(models.Model):
     category = models.ForeignKey(New_Category, on_delete=models.CASCADE)
     product_name = models.CharField(max_length=100,null=True,blank=True)
     product_price = models.DecimalField(max_digits=8, decimal_places=2,null=True,blank=True)
     product_image = models.ImageField(upload_to='images/')

     def __str__(self):
        return self.product_name or "Unnamed Product"
     
class Featured_Category(models.Model):
    category_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True,blank=True)
    description = models.CharField(max_length=500, null=True,blank=True)
    status = models.BooleanField(default=False,help_text="0-default,1-Hidden")
    def __str__(self):
        return self.category_name


class Featured_Products(models.Model):
     category = models.ForeignKey(Featured_Category, on_delete=models.CASCADE)
     product_name = models.CharField(max_length=100,null=True,blank=True)
     product_price = models.DecimalField(max_digits=8, decimal_places=2,null=True,blank=True)
     product_image = models.ImageField(upload_to='images/')

     def __str__(self):
        return self.product_name or "Unnamed Product"
     
     
class Career_Model(models.Model):    
    job_position = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    salary = models.IntegerField()
    job_details = RichTextField(max_length=20000)
    posted_date = models.DateField()
    end_date = models.DateTimeField()
    
    def is_active(self):
        return self.end_date >= timezone.now()
    


class Job_Application(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    pdf_file = models.FileField(upload_to='pdfs/')
    job_position = models.ForeignKey(Career_Model, on_delete=models.CASCADE, related_name='candidates', null=True)
    
    def _str_(self):
        return self.first_name