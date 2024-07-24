from django import forms

from .models import Enquiry_Model, Contact_Model, ProductCategory,Client_Review,Gold_Rate,NewCategory,ProductDetails,FeaturedCategory,FeaturedProducts,CareerModel,JobApplication,Collection_Model,SubCollections,Collection_Products,About_Video

class productForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry_Model
        fields = '__all__'

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client_Review
        fields = '__all__'

class GoldForm(forms.ModelForm):
    class Meta:
        model = Gold_Rate
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_Model
        fields = '__all__'
    

class Product_Form(forms.ModelForm):
    class Meta:
        model = NewCategory
        fields = '__all__'

class ProductDtailsForm(forms.ModelForm):
    class Meta:
        model = ProductDetails
        fields = '__all__'

class Featured_Form(forms.ModelForm):
    class Meta:
        model = FeaturedCategory
        fields = '__all__'

class Featured_Product_Form(forms.ModelForm):
    class Meta:
        model = FeaturedProducts
        fields = '__all__'

class CareerForm(forms.ModelForm):
    class Meta:
        model = CareerModel
        fields = '__all__'

class Job_Application_Form(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = '__all__'


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection_Model
        fields = '__all__'
    

class SubCollectionForm(forms.ModelForm):
    class Meta:
        model = SubCollections
        fields = '__all__'

class CollectionProductsForm(forms.ModelForm):
    class Meta:
        model = Collection_Products
        fields = '__all__'

class AboutVideoForm(forms.ModelForm):
    class Meta:
        model = About_Video
        fields = '__all__'