from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import ChatMessage, ClientReview, GoldRate , ContactModel, New_Category,Product_Details, Featured_Category, Featured_Products, Career_Model, Job_Application, CollectionModel ,Sub_Collections, CollectionProducts, AboutVideo
from .forms import  ClientForm, GoldForm, ContactForm,Product_Form,ProductDtailsForm, Featured_Form, Featured_Product_Form, CareerForm, Job_Application_Form, CollectionForm, SubCollectionForm, CollectionProductsForm, AboutVideoForm
from .models import ChatMessage
from django.core.mail import send_mail
from .forms import ContactForm
from django.http import JsonResponse
from django.utils import timezone
from django.conf import settings 

from django.http import Http404
# Create your views here.


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if 'previous_page' in request.session:
                previous_page = request.session['previous_page']
                del request.session['previous_page']
                return redirect(previous_page)
            else:
                return redirect('admin_dashboard')  # Redirect to default page
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('user_login')
    else:
        # Store the previous page in session
        if 'HTTP_REFERER' in request.META:
            request.session['previous_page'] = request.META['HTTP_REFERER']
    return render(request, 'authenticate/login.html')


def admin_dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'admin_pages/admin_dashboard.html')
    else:
        return redirect('user_login')

def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out"))
    return redirect('index')

def index(request):
    collections = CollectionModel.objects.all()
    sub_collections = Sub_Collections.objects.all()
    collection_products = CollectionProducts.objects.all()
    client_review = ClientReview.objects.all()
    rate = GoldRate.objects.all()
    product_category = New_Category.objects.all()
    product_details = Product_Details.objects.all()
    Featured_Products = Featured_Category.objects.all()
    video_links = AboutVideo.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('added')
    else:
        form = ContactForm()
    context = {
        'collections': collections,
        'sub_collections': sub_collections,
        'collection_products': collection_products,
        'client_review': client_review,
        'form': form,
        'rate': rate,
        'product_details': product_details,
        'product_category': product_category,
        'Featured_Products': Featured_Products,
        'video_links': video_links,
    }
    return render(request, 'index.html', context)


@login_required(login_url='user_login')
def add_product_category(request):
    if request.method == 'POST':
        form = Product_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_add_product_details') 
    else:
        form = Product_Form()

    return render(request, 'admin_pages/add_product_category.html', {'form': form})


@login_required(login_url='user_login')
def view_product_category(request):
    product = New_Category.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_product_category.html', {'product': product})


@login_required(login_url='user_login')
def update_product_category(request, id):
    product = get_object_or_404(New_Category, id=id)
    if request.method == 'POST':
        form = Product_Form(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('view_product_category')
    else:
        form = Product_Form(instance=product)
    return render(request, 'admin_pages/update_product_category.html', {'form': form, 'product': product})

@login_required(login_url='user_login')
def delete_product_category(request,id):
    product = New_Category.objects.get(id=id)
    product.delete()
    return redirect('view_product_category')


@login_required(login_url='user_login')
def admin_add_product_details(request):
    categories = New_Category.objects.all() 
    if request.method == 'POST':
        product_details = ProductDtailsForm(request.POST, request.FILES)
        if product_details.is_valid():
            product_details.save()
        
            return redirect('admin_view_product_details')  
    else:
        product_details = ProductDtailsForm()
   
    return render(request, 'admin_pages/admin_add_product_details.html', {'product_details': product_details,'categories':categories})

@login_required(login_url='user_login')
def admin_view_product_details(request):
    products = Product_Details.objects.all().order_by('-id')
    return render(request,'admin_pages/admin_view_product_details.html',{'products':products})

@login_required(login_url='user_login')
def admin_update_product_details(request, id):
    products = get_object_or_404(Product_Details, id=id)
    categories = New_Category.objects.all()  

    if request.method == 'POST':
        form = ProductDtailsForm(request.POST, request.FILES, instance=products)
        if form.is_valid():
            form.save()
            return redirect('admin_view_product_details')
    else:
        form = ProductDtailsForm(instance=products)

    return render(request, 'admin_pages/admin_update_product_details.html', {'form': form, 'products': products, 'categories': categories})

@login_required(login_url='user_login')
def admin_delete_product_details(request,id):
    products = Product_Details.objects.get(id=id)
    products.delete()
    return redirect('admin_view_product_details')

@login_required(login_url='user_login')
def add_featured_product_category(request):
    if request.method == 'POST':
        form = Featured_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_featured_details') 
    else:
        form = Featured_Form()

    return render(request, 'admin_pages/add_featured_product_category.html', {'form': form})

@login_required(login_url='user_login')
def view_featured_category(request):
    product = Featured_Category.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_featured_category.html', {'product': product})

@login_required(login_url='user_login')
def update_featured_category(request, id):
    product = get_object_or_404(Featured_Category, id=id)
    if request.method == 'POST':
        form = Featured_Form(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('view_featured_category')
    else:
        form = Featured_Form(instance=product)
    return render(request, 'admin_pages/update_featured_category.html', {'form': form, 'product': product})

@login_required(login_url='user_login')
def delete_featured_category(request,id):
    products = Featured_Category.objects.get(id=id)
    products.delete()
    return redirect('view_featured_category')

@login_required(login_url='user_login')
def add_featured_details(request):
    categories = Featured_Category.objects.all()
    if request.method == 'POST':
        details = Featured_Product_Form(request.POST, request.FILES)
        if details.is_valid():
            details.save()
            return redirect('view_featured_details')
    else:
        details = Featured_Product_Form()
    return render(request, 'admin_pages/add_featured_details.html', {'details': details, 'categories': categories})


@login_required(login_url='user_login')
def view_featured_details(request):
    products = Featured_Products.objects.all().order_by('-id')
    return render(request,'admin_pages/view_featured_details.html',{'products':products})

@login_required(login_url='user_login')
def update_featured_details(request, id):
    products = get_object_or_404(Featured_Products, id=id)
    categories = Featured_Category.objects.all()  

    if request.method == 'POST':
        form = Featured_Product_Form(request.POST, request.FILES, instance=products)
        if form.is_valid():
            form.save()
            return redirect('view_featured_details')
    else:
        form = Featured_Product_Form(instance=products)

    return render(request, 'admin_pages/update_featured_details.html', {'form': form, 'products': products, 'categories': categories})

@login_required(login_url='user_login')
def delete_featured_details(request,id):
    products = Featured_Products.objects.get(id=id)
    products.delete()
    return redirect('view_featured_details')

@login_required(login_url='user_login')
def view_enquiry(request):
    enquiry = ContactModel.objects.all().order_by('-id')
    return render(request,'admin_pages/view_enquiry.html',{'enquiry':enquiry})

@login_required(login_url='user_login')
def delete_enquiry(request,id):
    enquiry = ContactModel.objects.get(id=id)
    enquiry.delete()
    return redirect('view_enquiry')

@login_required(login_url='user_login')
def add_client_reviews(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_client_reviews') 
    else:
        form = ClientForm()

    return render(request, 'admin_pages/add_client_reviews.html', {'form': form})


@login_required(login_url='user_login')
def view_client_reviews(request):
    client_reviews = ClientReview.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_client_reviews.html', {'client_reviews': client_reviews})

@login_required(login_url='user_login')
def update_client_reviews(request, id):
    client_reviews = get_object_or_404(ClientReview, id=id)
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client_reviews)
        if form.is_valid():
            form.save()
            return redirect('view_client_reviews')
    else:
        form = ClientForm(instance=client_reviews)
    return render(request, 'admin_pages/update_client_reviews.html', {'form': form, 'client_reviews': client_reviews})


@login_required(login_url='user_login')
def delete_client_review(request,id):
    client_reviews = ClientReview.objects.get(id=id)
    client_reviews.delete()
    return redirect('view_client_reviews')

@login_required(login_url='user_login')
def add_gold_rate(request):
    if request.method == 'POST':
        form = GoldForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_gold_rate') 
    else:
        form = GoldForm()
    return render(request, 'admin_pages/add_gold_rate.html', {'form': form})

@login_required(login_url='user_login')
def view_gold_rate(request):
    gold_rate = GoldRate.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_gold_rate.html', {'gold_rate': gold_rate})

@login_required(login_url='user_login')
def update_gold_rate(request, id):
    gold_rate = get_object_or_404(GoldRate, id=id)
    if request.method == 'POST':
        form = GoldForm(request.POST, request.FILES, instance=gold_rate)
        if form.is_valid():
            form.save()
            return redirect('view_gold_rate')
    else:
        form = GoldForm(instance=gold_rate)
    return render(request, 'admin_pages/update_gold_rate.html', {'form': form, 'gold_rate': gold_rate})

@login_required(login_url='user_login')
def delete_gold_rate(request,id):
    gold_rate = GoldRate.objects.get(id=id)
    gold_rate.delete()
    return redirect('view_gold_rate')

@login_required(login_url='user_login')
def add_job_details(request):
    if request.method == 'POST':
        form = CareerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_job_details') 
    else:
        form = CareerForm()

    return render(request, 'admin_pages/add_job_details.html', {'form': form})

@login_required(login_url='user_login')
def view_job_details(request):
    job_details = Career_Model.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_job_details.html', {'job_details': job_details})

@login_required(login_url='user_login')
def update_job_details(request, id):
    job_details = get_object_or_404(Career_Model, id=id)
    if request.method == 'POST':
        form = CareerForm(request.POST, request.FILES, instance=job_details)
        if form.is_valid():
            form.save()
            return redirect('view_job_details')
    else:
        form = CareerForm(instance=job_details)
    return render(request, 'admin_pages/update_job_details.html', {'form': form, 'job_details': job_details})


@login_required(login_url='user_login')
def delete_job_details(request,id):
    job_details = Career_Model.objects.get(id=id)
    job_details.delete()
    return redirect('view_job_details')

@login_required(login_url='user_login')
def view_job_application(request):
    applications = Job_Application.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_job_application.html', {'applications': applications})

@login_required(login_url='user_login')
def delete_job_application(request, id):
    candidate = get_object_or_404(Job_Application, id=id)
    candidate.delete()
    return redirect('view_job_application')


@login_required(login_url='user_login')
def create_collections(request):
    
    if request.method == 'POST':
        form = CollectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create_sub_collections')  # Replace 'view_course' with your actual view name for viewing all courses
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = CollectionForm()  # Ensure you pass the correct form here
    
    return render(request, 'admin_pages/create_collections.html', {'form': form})

@login_required(login_url='user_login')
def view_collections(request):
    collections = CollectionModel.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_collections.html', {'collections': collections})

@login_required(login_url='user_login')
def update_collection(request, id):
    collection = get_object_or_404(CollectionModel, id=id)
    if request.method == 'POST':
        form = CollectionForm(request.POST, instance=collection)
        if form.is_valid():
            form.save()
            return redirect('view_collections')
    else:
        form = CollectionForm(instance=collection)
    return render(request, 'admin_pages/update_collection.html', {'form': form})

@login_required(login_url='user_login')
def delete_collection(request, id):
    collection = get_object_or_404(CollectionModel, id=id)   
    collection.delete()
    return redirect('view_collections')
    
@login_required(login_url='user_login')
def create_sub_collections(request):
    collections = CollectionModel.objects.all()
    if request.method == 'POST':
        form = SubCollectionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create_collection_products')  # Replace 'view_course' with your actual view name for viewing all courses
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = SubCollectionForm()  # Ensure you pass the correct form here
    
    return render(request, 'admin_pages/create_sub_collections.html', {'form': form,'collections':collections})

@login_required(login_url='user_login')
def view_sub_collections(request):
    sub_collections = Sub_Collections.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_sub_collections.html', {'sub_collections': sub_collections})


@login_required(login_url='user_login')
def update_sub_collection(request, id):
    sub_collection = get_object_or_404(Sub_Collections, id=id)
    if request.method == 'POST':
        form = SubCollectionForm(request.POST, request.FILES, instance=sub_collection)
        if form.is_valid():
            form.save()
            return redirect('view_sub_collections')  # Replace with the name of your view for viewing all sub-collections
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = SubCollectionForm(instance=sub_collection)
    
    return render(request, 'admin_pages/update_sub_collection.html', {'form': form})


@login_required(login_url='user_login')
def delete_sub_collection(request, id):
    sub_collection = get_object_or_404(Sub_Collections, id=id)
    sub_collection.delete()
    return redirect('view_sub_collections')  # Replace with the name of your view for viewing all sub-collections
    
@login_required(login_url='user_login')
def create_collection_products(request):
    collections = CollectionModel.objects.all()
    sub_collections = Sub_Collections.objects.all()
    
    if request.method == 'POST':
        form = CollectionProductsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_collection_products')  # Redirect after successful form submission
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = CollectionProductsForm()  # Initialize the form

    return render(request, 'admin_pages/create_collection_products.html', {
        'form': form,
        'collections': collections,
        'sub_collections': sub_collections
    })

@login_required(login_url='user_login')
def load_sub_collections(request):
    collection_id = request.GET.get('collection_id')
    sub_collections = Sub_Collections.objects.filter(collection_id=collection_id).values('id', 'sub_collection_type')
    return JsonResponse(list(sub_collections), safe=False)

@login_required(login_url='user_login')
def view_collection_products(request):
    products = CollectionProducts.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_collection_products.html', {'products': products})

@login_required(login_url='user_login')
def update_collection_product(request, id):
    product = get_object_or_404(CollectionProducts, id=id)
    collections = CollectionModel.objects.all()
    sub_collections = Sub_Collections.objects.filter(collection=product.collections)
    
    if request.method == 'POST':
        form = CollectionProductsForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('view_collection_products')
    else:
        form = CollectionProductsForm(instance=product)
    
    return render(request, 'admin_pages/update_collection_product.html', {
        'form': form,
        'collections': collections,
        'sub_collections': sub_collections,
    })

@login_required(login_url='user_login')
def load_sub_collections(request):
    collection_id = request.GET.get('collection_id')
    sub_collections = Sub_Collections.objects.filter(collection_id=collection_id)
    data = list(sub_collections.values('id', 'sub_collection_type'))
    return JsonResponse(data, safe=False)

@login_required(login_url='user_login')
def delete_collection_product(request, id):
    product = get_object_or_404(CollectionProducts, id=id)
    product.delete()
    return redirect('view_collection_products')


@login_required(login_url='user_login')
def create_about_video(request):
    if request.method == 'POST':
        form = AboutVideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_about_video') 
    else:
        form = AboutVideoForm()

    return render(request, 'admin_pages/create_about_video.html', {'form': form})
    

def view_about_video(request):
    links = AboutVideo.objects.all()
    return render(request,'admin_pages/view_about_video.html',{'links':links})
    

@login_required(login_url='user_login')
def update_about_video(request, id):
    video = get_object_or_404(AboutVideo, id=id)

    if request.method == 'POST':
        form = AboutVideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            return redirect('view_about_video')
    else:
        form = AboutVideoForm(instance=video)

    return render(request, 'admin_pages/update_about_video.html', {'form': form})

@login_required(login_url='user_login')
def delete_about_video(request, id):
    video = get_object_or_404(AboutVideo, id=id)
    video.delete()
    return redirect('view_about_video')

# Chatbot Section
from django.http import JsonResponse
from .models import ChatMessage

@login_required(login_url='user_login')
def chatbot_message_view(request):
    chatbot = ChatMessage.objects.all().order_by('-id')
    return render(request,'admin_pages/chatbot_message_view.html',{'chatbot':chatbot})

@login_required(login_url='user_login')
def delete_message(request,id):
    chatbot = ChatMessage.objects.get(id=id)
    chatbot.delete()
    return redirect('chatbot_message_view')
    
#  //////// #


def submit_query(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and phone_number and email and message:
            # Save the data to the ChatMessage model
            ChatMessage.objects.create(
                name=name,
                phone_number=phone_number,
                email=email,
                message=message
            )
            return JsonResponse({'message': 'Data saved successfully'}, status=200)
        else:
            return JsonResponse({'error': 'All fields are required'}, status=400)



def Product_details(request,category_name):
    category = New_Category.objects.all()
    if(New_Category.objects.filter(category_name=category_name, status=0)):
        product_details = Product_Details.objects.filter(category__category_name=category_name)
        category_name = New_Category.objects.filter(category_name=category_name).first()
        context = {'product_details': product_details,'category_name':category_name,'category':category}
        return render(request,"Product_details.html",context)
    else:
        messages.warning(request,"No such category found")
    return render(request,'Product_details.html')


def featured_products(request,category_name):
    category = Featured_Category.objects.all()
    if(Featured_Category.objects.filter(category_name=category_name, status=0)):
        product_details = Featured_Products.objects.filter(category__category_name=category_name)
        category_name = Featured_Category.objects.filter(category_name=category_name).first()
        context = {'product_details': product_details,'category_name':category_name,'category':category}
        return render(request,"Featured_Product_details.html",context)
    else:
        messages.warning(request,"No such category found")
    return render(request,'Featured_Product_details.html')




def collection_products(request, collection_type, sub_collection_type):
    collections = CollectionModel.objects.all()
    sub_collections = Sub_Collections.objects.all()
    collection = get_object_or_404(CollectionModel, collection_type=collection_type)
    sub_collection = get_object_or_404(Sub_Collections, sub_collection_type=sub_collection_type, collection=collection)
    details = CollectionProducts.objects.filter(
        collections=collection, 
        sub_collection=sub_collection
    )
    # Debugging
    print(f'Collection: {collection}')
    print(f'Sub-Collection: {sub_collection}')
    print(f'Products Count: {details.count()}')
    
    for product in details:
        print(f'Product Name: {product.product_name or "No Name"}, Image: {product.image.url if product.image else "No Image"}')

    # Prepare the context
    context = {
        'collection': collection,
        'sub_collection': sub_collection,
        'details': details,
        'collections':collections,
        'sub_collections':sub_collections
    }
    return render(request, 'collection_products.html', context)



def job_application(request):
    # job_positions = Career_Model.objects.all()
    job_positions = Career_Model.objects.filter(end_date__gte=timezone.now())
    if request.method == 'POST':
        form = Job_Application_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your application has been submitted successfully!')
            return redirect('job_application')          
    else:
        form = Job_Application_Form()

    return render(request, 'application.html', {'form': form,'job_positions':job_positions})


def generate_certificate_url(id):
    try:
        certificate = Job_Application.objects.get(id1=id)
        return f'{settings.MEDIA_URL}{certificate.pdf_file}'
    except Job_Application.DoesNotExist:
        return None


def contact(request):
    collections = CollectionModel.objects.all()
    sub_collections = Sub_Collections.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form,'collections':collections,'sub_collections':sub_collections})


def about(request):
    data = ClientReview.objects.all()
    collections = CollectionModel.objects.all()
    sub_collections = Sub_Collections.objects.all()
    video_links = AboutVideo.objects.all()
    return render(request,'about.html',{'data':data,'video_links':video_links,'collections':collections,'sub_collections':sub_collections})

def contact_new(request):
    return render(request,'contact-new.html')


def careers(request):
    collections = CollectionModel.objects.all()
    sub_collections = Sub_Collections.objects.all()
    jobs = Career_Model.objects.filter(end_date__gte=timezone.now())
    return render(request, 'career.html', {'jobs': jobs,'collections':collections,'sub_collections':sub_collections})

def job_details(request,job_position):
    collections = CollectionModel.objects.all()
    sub_collections = Sub_Collections.objects.all()
    job_details = get_object_or_404(Career_Model, job_position=job_position)
    return render(request,'job_details.html',{'job_details':job_details,'collections':collections,'sub_collections':sub_collections})

   
def application(request):
    return render(request,'application.html')

