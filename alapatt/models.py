from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
# Create your models here.

class Enquiry_Model(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    subject = models.CharField(max_length=200, null=True, blank=True)
    comment = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Contact_Model(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False,help_text="0-default,1-Hidden")

    def __str__(self):
        return self.name


class Chat_Message(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
    
    
class Client_Review(models.Model):
    client_name = models.CharField(max_length=100, null=True, blank=True)
    client_image = models.ImageField(upload_to='client_images/', null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    review_video = models.FileField(upload_to='review_videos/', null=True, blank=True)
    def __str__(self):
        return self.client_name


class Gold_Rate(models.Model):
    gold_rate = models.DecimalField(max_digits=8, decimal_places=2)
    

class NewCategory(models.Model):
    category_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True,blank=True)
    description = models.CharField(max_length=500, null=True,blank=True)
    status = models.BooleanField(default=False,help_text="0-default,1-Hidden")

    def __str__(self):
        return self.category_name
    
class ProductDetails(models.Model):
     category = models.ForeignKey(NewCategory, on_delete=models.CASCADE)
     product_name = models.CharField(max_length=100,null=True,blank=True)
     product_price = models.DecimalField(max_digits=8, decimal_places=2,null=True,blank=True)
     product_image = models.ImageField(upload_to='images/')

     def __str__(self):
        return self.product_name or "Unnamed Product"
     
class FeaturedCategory(models.Model):
    category_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True,blank=True)
    description = models.CharField(max_length=500, null=True,blank=True)
    status = models.BooleanField(default=False,help_text="0-default,1-Hidden")
    def __str__(self):
        return self.category_name


class FeaturedProducts(models.Model):
     category = models.ForeignKey(FeaturedCategory, on_delete=models.CASCADE)
     product_name = models.CharField(max_length=100,null=True,blank=True)
     product_price = models.DecimalField(max_digits=8, decimal_places=2,null=True,blank=True)
     product_image = models.ImageField(upload_to='images/')

     def __str__(self):
        return self.product_name or "Unnamed Product"
     
     
class CareerModel(models.Model):    
    job_position = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    salary = models.IntegerField()
    job_details = models.TextField()
    posted_date = models.DateField()
    end_date = models.DateTimeField()
    
    def is_active(self):
        return self.end_date >= timezone.now()
    


class JobApplication(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    pdf_file = models.FileField(upload_to='pdfs/')
    job_position = models.ForeignKey(CareerModel, on_delete=models.CASCADE, related_name='candidates', null=True)
    
    def _str_(self):
        return self.first_name


class Collection_Model(models.Model):
    class CollectionTypes(models.TextChoices):
        GOLD = 'Gold', 'Gold'
        DIAMOND = 'Diamond', 'Diamond'
        PRECIOUS_STONE = 'Precious Stone', 'Precious Stone'

    collection_type = models.CharField(
        max_length=50,
        choices=CollectionTypes.choices,
        default=CollectionTypes.GOLD,
    )
    def __str__(self):
        return self.collection_type

class SubCollections(models.Model):
    class SubCollection(models.TextChoices):
        RING = 'ring', 'Ring'
        NECKLACE = 'necklace', 'Necklace'
        ANKLET = 'anklet', 'Anklet'
        BANGLES = 'bangles', 'Bangles'
        BRACELET = 'bracelet', 'Bracelet'
        CHAIN = 'chain', 'Chain'
        EARRINGS = 'earrings', 'Earrings'
        PENDANTS = 'pendants', 'Pendants'

    sub_collection_type = models.CharField(
        max_length=50,
        choices=SubCollection.choices,
        default=SubCollection.RING,
    )
    collection = models.ForeignKey(Collection_Model, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.sub_collection_type

class Collection_Products(models.Model):
    product_name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    collections = models.ForeignKey(Collection_Model, on_delete=models.CASCADE)
    sub_collection = models.ForeignKey(SubCollections, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product_name or 'Unnamed Product'

    
class About_Video(models.Model):
    video_link = models.URLField(max_length=200, unique=True, null=True, blank=True)

    

 
 
