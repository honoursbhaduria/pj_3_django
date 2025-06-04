from django.shortcuts import render , redirect , get_object_or_404

from .models import *
from .forms import ProductForm 
from django.http import HttpResponse

def product_list(request):
    products = product.objects.all()
    return render(request, 'myapp/index.html',{products:products})

def product_detail(request, pk):
    product = get_object_or_404(product, pk=pk)
    return render(request, 'myapp/index2.html',{product:product})

def edit_product(request, pk ):
    product = get_object_or_404(product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')

    else:
        form  = ProductForm(instance=product)
    return render(request, 'myapp/delete.html', {'product':product})

def home(request):
    return render("hello world")

