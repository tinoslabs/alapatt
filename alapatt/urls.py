"""
URL configuration for alapattfashion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [

    path('', views.index, name='index'),

    path('user_login',views.user_login,name='user_login'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),

    path('submit_query/',views.submit_query, name='submit_query'),
    path('chatbot_message_view',views.chatbot_message_view,name='chatbot_message_view'),
    path('delete_message/<int:id>/',views.delete_message,name='delete_message'),
  
    path('create_collections/', views.create_collections, name='create_collections'),
    path('view_collections/', views.view_collections, name='view_collections'),
    path('update_collection/<int:id>/', views.update_collection, name='update_collection'),
    path('delete_collection/<int:id>/', views.delete_collection, name='delete_collection'),
    
    path('create_sub_collections',views.create_sub_collections,name='create_sub_collections'),
    path('view_sub_collections', views.view_sub_collections, name='view_sub_collections'),
    path('update_sub_collection/<int:id>/', views.update_sub_collection, name='update_sub_collection'),
    path('delete_sub_collection/<int:id>/', views.delete_sub_collection, name='delete_sub_collection'),

    path('create_collection_products',views.create_collection_products,name='create_collection_products'),
    path('load_sub_collections', views.load_sub_collections, name='load_sub_collections'),
    path('view_collection_products',views.view_collection_products,name='view_collection_products'),
    path('update_collection_product/<int:id>/', views.update_collection_product, name='update_collection_product'),
    path('delete_collection_product/<int:id>/', views.delete_collection_product, name='delete_collection_product'),
    
    path('load-sub-collections/', views.load_sub_collections, name='load_sub_collections'),
    path('collections/<str:collection_type>/<str:sub_collection_type>/', views.collection_products, name='collection_products'),

    path('create_about_video',views.create_about_video,name='create_about_video'),
    path('view_about_video',views.view_about_video,name='view_about_video'),
    path('update/<int:id>/', views.update_about_video, name='update_about_video'),
    path('delete/<int:id>/', views.delete_about_video, name='delete_about_video'),
    

    path('contact/', views.contact, name='contact'),
    path('view_enquiry',views.view_enquiry, name='view_enquiry'),
    path('delete_enquiry/<int:id>', views.delete_enquiry, name='delete_enquiry'),


    path('add_product_category', views.add_product_category, name='add_product_category'),
    path('view_product_category', views.view_product_category, name='view_product_category'),
    path('update_product_category/<int:id>/', views.update_product_category, name='update_product_category'),
    path('delete_product_category/<int:id>/', views.delete_product_category, name='delete_product_category'),

    path('admin_add_product_details', views.admin_add_product_details, name='admin_add_product_details'),
    path('admin_view_product_details', views.admin_view_product_details, name='admin_view_product_details'),
    path('Product_details/<str:category_name>/',views.Product_details,name='Product_details'),
    path('admin_update_product_details/<int:id>/',views.admin_update_product_details,name='admin_update_product_details'),
    path('admin_delete_product_details/<int:id>/',views.admin_delete_product_details,name='admin_delete_product_details'),

    path('add_featured_product_category',views.add_featured_product_category,name='add_featured_product_category'),
    path('view_featured_category', views.view_featured_category, name='view_featured_category'),
    path('update_featured_category/<int:id>/', views.update_featured_category, name='update_featured_category'),
    path('delete_featured_category/<int:id>/', views.delete_featured_category, name='delete_featured_category'),

    path('add_featured_details', views.add_featured_details, name='add_featured_details'),
    path('view_featured_details', views.view_featured_details, name='view_featured_details'),
    path('update_featured_details/<int:id>/', views.update_featured_details, name='update_featured_details'),
    path('delete_featured_details/<int:id>/', views.delete_featured_details, name='delete_featured_details'),

    path('featured_products/<str:category_name>/', views.featured_products, name='featured_products'),

   
    
    path('add_client_reviews', views.add_client_reviews, name='add_client_reviews'),
    path('view_client_reviews', views.view_client_reviews, name='view_client_reviews'),
    path('update_client_reviews/<int:id>/', views.update_client_reviews, name='update_client_reviews'),
    path('delete_client_review/<int:id>/', views.delete_client_review, name='delete_client_review'),

    path('add_gold_rate', views.add_gold_rate, name='add_gold_rate'),
    path('view_gold_rate', views.view_gold_rate, name='view_gold_rate'),
    path('update_gold_rate/<int:id>/', views.update_gold_rate, name='update_gold_rate'),
    path('delete_gold_rate/<int:id>/', views.delete_gold_rate, name='delete_gold_rate'),

    path('about', views.about, name='about'),
    path('contact_new', views.contact_new, name='contact_new'),
    # path('login', views.login, name='login'),

    
    path('careers', views.careers, name='careers'),
    path('add_job_details', views.add_job_details, name='add_job_details'),
    path('view_job_details', views.view_job_details, name='view_job_details'),
    path('update_job_details/<int:id>/', views.update_job_details, name='update_job_details'),
    path('delete_job_details/<int:id>/', views.delete_job_details, name='delete_job_details'),

    path('job_details/<str:job_position>/',views.job_details,name='job_details'),
    path('job_application', views.job_application, name='job_application'),

    path('view_job_application', views.view_job_application, name='view_job_application'),
    path('delete_job_application/<int:id>/',views.delete_job_application, name='delete_job_application'),
    path('application',views.application, name='application'),
]
