from django.db import models

# Create your models here.

class EnquiryModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    subject = models.CharField(max_length=200, null=True, blank=True)
    comment = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
    

class product_category(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False,help_text="0-default,1-Hidden")

    def __str__(self):
        return self.name


class sub_category(models.Model):
    category = models.ForeignKey(product_category,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100, null=True, blank=True)
    status = models.BooleanField(default=False,help_text="0-default,1-Hidden")

    def __str__(self):
        return self.product_name if self.product_name else "No Product Name"


class ProductDetails(models.Model):
    product_category = models.ForeignKey(product_category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(sub_category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='project_images/')
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
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
    