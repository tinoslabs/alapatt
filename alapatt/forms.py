from django import forms
from .models import product_category, sub_category, ProductDetails, EnquiryModel, ClientReview, GoldRate, ContactModel, New_Category,Product_Details,ContactModel

class productForm(forms.ModelForm):
    class Meta:
        model = product_category
        fields = '__all__'

class sub_category_Form(forms.ModelForm):
    class Meta:
        model = sub_category
        fields = '__all__'

class product_details_Form(forms.ModelForm):
    class Meta:
        model = ProductDetails
        fields = '__all__'

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = EnquiryModel
        fields = '__all__'

class ClientForm(forms.ModelForm):
    class Meta:
        model = ClientReview
        fields = '__all__'

class GoldForm(forms.ModelForm):
    class Meta:
        model = GoldRate
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'
    

class Product_Form(forms.ModelForm):
    class Meta:
        model = New_Category
        fields = '__all__'

class ProductDtailsForm(forms.ModelForm):
    class Meta:
        model = Product_Details
        fields = '__all__'