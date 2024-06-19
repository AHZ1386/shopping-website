from Store.models import Order, Product, Category, Brand
from django.shortcuts import render
from  Account.models import User
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import forms
from django.http import Http404
from django.contrib.auth.decorators import user_passes_test
from .decorator import superuser_required


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    context = {
        'orders': Order.objects.exclude(status='do').count(),
        'users': User.objects.all().count(),
        'products': Product.objects.count(),

    }
    return render(request, 'Custom_admin/index.html',context)

class ProductUpdateView(UpdateView):
    model = Product
    form_class = forms.ProductUpdateForm
    template_name = 'Custom_admin/Product/product_update.html'
    success_url = '/custom-admin/products/'

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 20
    template_name = 'Custom_admin/Product/product_list.html'

class OrderListView(ListView):
    model = Order
    context_object_name = 'orders'
    paginate_by = 10
    template_name = 'Custom_admin/Order/order_list.html'


class UserListView(ListView):
    model = User
    context_object_name = 'users'
    paginate_by = 30
    template_name = 'Custom_admin/User/user_list.html'



class ProductCreateView(CreateView):
    model = Product
    form_class = forms.ProductCreateForm
    template_name = 'Custom_admin/Product/product_create.html'
    success_url = '/custom-admin/products/'



class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'Custom_admin/Product/product_delete.html'
    success_url = '/custom-admin/products/'

class OrderUpdateView(UpdateView):
    model = Order
    form_class = forms.OrderUpdateForm
    template_name = 'Custom_admin/Order/order_update.html'
    success_url = '/custom-admin/orders/'

class BrandCreateView(CreateView):
    model = Brand
    form_class = forms.BrandCreateForm
    template_name = 'Custom_admin/Product/brand_create.html'
    success_url = '/custom-admin/'

class CategoryCreateView(CreateView):
    model = Category
    form_class = forms.CategoryCreateForm
    template_name = 'Custom_admin/Product/category_create.html'
    success_url = '/custom-admin/'