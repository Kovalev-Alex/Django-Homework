from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    phone_object = Phone.objects.all()
    phone_name = (p.name for p in phone_object)
    phone_price = (p.price for p in phone_object)
    phone_image = (p.image for p in phone_object)
    
    
    context = {
        'phones': {
            'name': phone_name,
            'price': phone_price,
            'image': phone_image

        }
    }
    
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {

    }
    return render(request, template, context)
 
