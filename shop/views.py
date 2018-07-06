from django.shortcuts import render,get_object_or_404
from .models import Product,Category
from django.conf import settings
from cart.forms import CartAddProductForm


# Create your views here.

#Страница с товарами
def ProductList(request,category_slug=None):
    category=None
    categories=Category.objects.all()
    products=Product.objects.filter(available=True)
    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)
        products=products.filter(category=category)
    context={'categories':categories,'products':products,'category':category}
    return render(request,'shop/product/ProductList.html',context)
#Страница Товара
def ProductDetail(request,id,slug):
    product=get_object_or_404(Product,id=id,slug=slug,available=True)
    cart_product_form=CartAddProductForm()
    return render(request,'shop/product/detail.html',{'product':product,'cart_product_form':cart_product_form})
