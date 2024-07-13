from django import forms
from .models import product_category, EnquiryModel, ClientReview, GoldRate, ContactModel, New_Category,Product_Details,ContactModel,Featured_Category,Featured_Products,Career_Model, Job_Application

class productForm(forms.ModelForm):
    class Meta:
        model = product_category
        fields = '__all__'

# class Collections_Form(forms.ModelForm):
#     class Meta:
#         model = collections_category
#         fields = '__all__'

# class sub_category_Form(forms.ModelForm):
#     class Meta:
#         model = sub_category
#         fields = '__all__'

# class collections_details_form(forms.ModelForm):
#     class Meta:
#         model = Collections_Details
#         fields = '__all__'

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

class Featured_Form(forms.ModelForm):
    class Meta:
        model = Featured_Category
        fields = '__all__'

class Featured_Product_Form(forms.ModelForm):
    class Meta:
        model = Featured_Products
        fields = '__all__'

class CareerForm(forms.ModelForm):
    class Meta:
        model = Career_Model
        fields = '__all__'

class Job_Application_Form(forms.ModelForm):
    class Meta:
        model = Job_Application
        fields = '__all__'

