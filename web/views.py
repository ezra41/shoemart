from django.shortcuts import render
from . models import Product
from . models import Collection,form
from . models import Shopping


  


# Create your views here.
def index(request):
    context={
        'product':Product.objects.all(),
        'collection':Collection.objects.all()
        

    }
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')

        customer = form(
            name=name,
            message=message,
            email=email,
            phone=phone
        )
        customer.save()

    return render(request,'web/index.html',context)
    
def about(request):
    context={
        'product':Product.objects.all(),
        'collection':Collection.objects.all()

    }

    return render(request,'web/about.html',context)
def contact(request):
    
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')

        customer = form(
            name=name,
            message=message,
            email=email,
            phone=phone
        )
        customer.save()
    

    return render(request,'web/contact.html')
def shoemart(request):
    context={
    
         'shopping':Shopping.objects.all()
     }
    return render(request,'web/shoemart.html',context)
