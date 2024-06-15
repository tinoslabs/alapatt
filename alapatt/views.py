from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import product_category, sub_category, ProductDetails, EnquiryModel, ChatMessage, ClientReview, GoldRate
from .models import ProductDetails
from .forms import productForm,sub_category_Form, sub_category_Form, product_details_Form, EnquiryForm, ClientForm, GoldForm
from .models import ChatMessage
# Create your views here.


# def user_login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('admin_dashboard')
#         else:
#             messages.error(request, "Invalid username or password. Please try again....")
#             print("Invalid login attempt") 
#             return redirect('user_login')
#     return render(request, 'authenticate/login.html')

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


# def login(request):
#     return render(request,'login.html')

# def admin_dashboard(request):
#     return render(request, 'admin_pages/admin_dashboard.html')

def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out"))
    return redirect('index')

def index(request):
    client_review = ClientReview.objects.all()
    rate = GoldRate.objects.all()
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)  # Print form errors to console for debugging
            return HttpResponse(f"Form is invalid: {form.errors}")  # Return form errors in HTTP response for debugging
    else:
        form = EnquiryForm()
    return render(request, 'index.html', {'client_review': client_review, 'form': form, 'rate':rate})

def test(request):
    return render(request, 'test.html') 

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


def category_grid(request):
    categories = product_category.objects.all()
    subcategory = sub_category.objects.all()
    return render(request, 'category-grid.html',{'categories':categories, 'subcategory':subcategory})

# def product_details(request, product_id):
#     product = get_object_or_404(ProductDetails, id=product_id)
#     return render(request, 'product-details.html', {'product': product})

# def product_details(request, subcategory_id):
#     subcategory = get_object_or_404(sub_category, id=subcategory_id)
#     products = ProductDetails.objects.filter(sub_category=subcategory, status=False)
#     return render(request, 'product-details.html', {'subcategory': subcategory, 'products': products})

def product_list(request, category_id, subcategory_id=None):
    category = get_object_or_404(product_category, id=category_id)
    subcategory = None
    if subcategory_id:
        subcategory = get_object_or_404(sub_category, id=subcategory_id, category=category)
        products = ProductDetails.objects.filter(product_category=category, sub_category=subcategory, status=True)
    else:
        products = ProductDetails.objects.filter(product_category=category, status=True)
    
    return render(request, 'product_list.html', {
        'category': category,
        'subcategory': subcategory,
        'products': products
    })
# diamod section start #

def diamond_anklet(request):
    return render(request, 'diamond/anklet.html')

def diamond_bangles(request):
    return render(request, 'diamond/bangles.html')

def diamond_bracelet(request):
    return render(request, 'diamond/bracelet.html')

def diamond_chain(request):
    return render(request, 'diamond/chain.html')

def diamond_earrings(request):
    return render(request, 'diamond/earrings.html')

def diamond_necklace(request):
    return render(request, 'diamond/necklace.html')

def diamond_pendants(request):
    return render(request, 'diamond/pendants.html')

def diamond_ring(request):
    return render(request, 'diamond/ring.html')


# gold section start #

def gold_anklet(request):
    return render(request, 'gold/anklet.html')

def gold_bangles(request):
    return render(request, 'gold/bangles.html')

def gold_bracelet(request):
    return render(request, 'gold/bracelet.html')

def gold_chain(request):
    return render(request, 'gold/chain.html')

def gold_earrings(request):
    return render(request, 'gold/earrings.html')

def gold_necklace(request):
    return render(request, 'gold/necklace.html')

def gold_pendants(request):
    return render(request, 'gold/pendants.html')

def gold_ring(request):
    return render(request, 'gold/ring.html')

# loram ipsum dolor section start #

def stone_anklet(request):
    return render(request, 'precious_stone/anklet.html')

def stone_bangles(request):
    return render(request, 'precious_stone/bangles.html')

def stone_bracelet(request):
    return render(request, 'precious_stone/bracelet.html')

def stone_chain(request):
    return render(request, 'precious_stone/chain.html')

def stone_earrings(request):
    return render(request, 'precious_stone/earrings.html')

def stone_necklace(request):
    return render(request, 'precious_stone/necklace.html')

def stone_pendants(request):
    return render(request, 'precious_stone/pendants.html')

def stone_ring(request):
    return render(request, 'precious_stone/ring.html')

def category_list(request):
    return render(request, 'category-list.html')



@login_required(login_url='user_login')
def add_product_category(request):
    if request.method == 'POST':
        form = productForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_sub_category') 
    else:
        form = productForm()

    return render(request, 'admin_pages/add_product_category.html', {'form': form})

@login_required(login_url='user_login')
def view_product_category(request):
    product = product_category.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_product_category.html', {'product': product})

@login_required(login_url='user_login')
def update_product_category(request,id):
    product = get_object_or_404(product_category, id=id)
    if request.method == 'POST':
        form = productForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('view_product_category')
    else:
        form = productForm(instance=product)
    return render(request, 'admin_pages/update_product_category.html', {'form': form, 'product': product})

@login_required(login_url='user_login')
def delete_product_category(request,id):
    product = product_category.objects.get(id=id)
    product.delete()
    return redirect('view_product_category')

@login_required(login_url='user_login')
def add_sub_category(request):
    categories = product_category.objects.all()
    if request.method == 'POST':
        form = sub_category_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_product_details') 
    else:
        form = sub_category_Form()

    return render(request, 'admin_pages/add_sub_category.html', {'form': form, 'categories':categories})


@login_required(login_url='user_login')
def view_sub_category(request):
    data = sub_category.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_sub_category.html', {'data': data})


@login_required(login_url='user_login')
def update_sub_category(request,id):
    categories = product_category.objects.all()
    data = get_object_or_404(sub_category, id=id)
    if request.method == 'POST':
        form = sub_category_Form(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('view_sub_category')
    else:
        form = sub_category_Form(instance=data)
    return render(request, 'admin_pages/update_sub_category.html', {'form': form, 'data': data, 'categories':categories})

@login_required(login_url='user_login')
def delete_sub_category(request,id):
    product = sub_category.objects.get(id=id)
    product.delete()
    return redirect('add_product_details')

# @login_required(login_url='user_login')
# def add_product_details(request):
#     categories = product_category.objects.all()
#     category = sub_category.objects.all()
#     if request.method == 'POST':
#         form = product_details_Form(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('view_product_details') 
#     else:
#         form = product_details_Form()

#     return render(request, 'admin_pages/add_product_details.html', {'form': form, 'categories':categories,'category':category})


# def add_product_details(request):
#     categories = product_category.objects.all()
#     subcategories = sub_category.objects.all()
#     if request.method == 'POST':
#         form = product_details_Form(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('view_product_details')
#     else:
#         form = product_details_Form()

#     return render(request, 'admin_pages/add_product_details.html', {
#         'form': form,
#         'categories': categories,
#         'subcategories': subcategories
#     })

def add_product_details(request):
    categories = product_category.objects.all()
    subcategories = sub_category.objects.all()
    if request.method == 'POST':
        form = product_details_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_product_details')
    else:
        form = product_details_Form()

    return render(request, 'admin_pages/add_product_details.html', {
        'form': form,
        'categories': categories,
        'subcategories': subcategories
    })



def view_product_details(request):
    details = ProductDetails.objects.all()
    return render(request, 'admin_pages/view_product_details.html', {'details': details})



@login_required(login_url='user_login')
def update_product_details(request,id):
    categories = product_category.objects.all()
    subcategorty = sub_category.objects.all()
    data = get_object_or_404(ProductDetails, id=id)
    if request.method == 'POST':
        form = sub_category_Form(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('view_product_details')
    else:
        form = sub_category_Form(instance=data)
    return render(request, 'admin_pages/update_sub_category.html', {'form': form, 'data': data, 'categories':categories,'subcategorty':subcategorty})


@login_required(login_url='user_login')
def delete_product_details(request,id):
    product = ProductDetails.objects.get(id=id)
    product.delete()
    return redirect('view_product_details')


def contact(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = EnquiryForm()
    return render(request, 'contact.html', {'form': form})

@login_required(login_url='user_login')
def view_enquiry(request):
    enquiry = EnquiryModel.objects.all().order_by('-id')
    return render(request,'admin_pages/view_enquiry.html',{'enquiry':enquiry})

@login_required(login_url='user_login')
def delete_contact(request,id):
    enquiry = EnquiryModel.objects.get(id=id)
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

def about_1(request):
    return render(request,'about-1.html')

def about(request):
    return render(request,'about.html')

def testimonial(request):
    return render(request,'testimonial.html')

def demo(request):
    return render(request,'demo.html')

def contact_new(request):
    return render(request,'contact-new.html')
