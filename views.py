
from django.shortcuts import render,HttpResponse
from  .models import Product
from math import ceil
from django.contrib import messages
from .models import Contact 
from .models import Orders

from .models import OrderUpdate

from datetime import datetime
import logging
# from .models import Category


# Create your views here.
# def index(request):
#     products=Product.objects.all() 
#     params={'products':products}
#     return render(request,"index.html",params)
def about(request):
    return render(request,'about.html')
def contact(request):
     return render(request,'contact.html')    
def tracker(request):
     return render(request,'tracker.html')  
 
# def productview(request):
#      feedbackData=Product.objects.all()
#      data={
#          'feedbackData':feedbackData
#     } 
    
     return render(request,'prodview.html',data)               
# def checkout(request):
#      return render(request,'checkout.html')       

def index(request):
     feedbackData=Product.objects.all()  
     data={
         'feedbackData':feedbackData
    }   
     n = len(feedbackData)
     nSlides = n//4 + ceil((n/4)-(n//4))
     # params = {'no_of_slides':nSlides, 'range': range(1,nSlides)}
     
     return render(request,'index.html',data)      

# def index(request):
#        Data=Category.objects.all()  
#        data={
#           'Data':Data
#       }   
#        return render(request,'index.html',data)    

def productView(request, myid):
    product=Product.objects.filter(id=myid)
    print(product)
    return render(request, "prodview.html",{'product':product[0]})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'your message has been sent!')
    return render(request,'contact.html')    

def checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')

        order = Orders(items_json= items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        update= OrderUpdate(order_id= order.order_id, update_desc="The order has been placed")
        update.save()
        thank=True
        id=order.order_id
        return render(request, 'checkout.html', {'thank':thank, 'id':id})
    return render(request, 'checkout.html')    

def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query)<4:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'search.html', params)        
