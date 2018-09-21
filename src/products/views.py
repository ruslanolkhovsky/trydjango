from django.http import Http404
from django.urls import reverse

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.

# An example of direct build Views
#
#

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm() #re-render the form after save to cleanup the fields!
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/product_list.html", context)


def product_detail_view (request, id):
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404
    #

    #  Or better to use the get_object_or_404 method
    obj = get_object_or_404(Product, id=id)

    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)


def product_delete_view (request, id):
    obj = get_object_or_404(Product, id=id)
    #POST request
    if request.method == "POST":
        obj.delete()
        return redirect('/products')
    context = {
        'object': obj
    }
    return render(request, "products/product_delete.html", context)

def product_update_view(request, id):
    # initial_data = {
    #     'title': "My awesome title"
    # }
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj) # initial=initial_data,
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)
