from django.shortcuts import render
from django.http import HttpResponse
from company.models import *
from login.models import *
from django.shortcuts import render, get_object_or_404, redirect
from .models import *

def delete_stock(request, id):
    q1 = Stocks.objects.get(id=id)
    q1.delete()
    q2 = LogInventory(user=q1.user, product=q1.product, quantity=q1.quantity, operation='DELETE')
    q2.save()
    return redirect('inventory:stock')


def stock(request):
    user = Register.objects.get(email=request.session['username'])
    q1 = Stocks.objects.filter(user=user)
    return render(request, 'inventory/home.html', {'stock': q1})

def add_stock(request, id):
    if request.method == 'POST':
        quantity = request.POST['quantity']

    product = Product.objects.get(id=id)
    customer = request.session['username']
    customer = Register.objects.get(email=customer)
    q1 = None
    try:
        q1 = Stocks.objects.get(product=product)
    except:
        pass

    if q1:
        q1.quantity += int(quantity)
        q1.save()
    else:
        Stock = Stocks(product=product, user=customer, quantity=quantity)
        Stock.save()
    q2 = LogInventory(user=customer, product=product, quantity=quantity, operation='STOCKIN')
    q2.save()
    return redirect('inventory:product_list')

def product_list_company(request, slug=None):
    category = None
    company = None
    q1 = Register.objects.get(email=request.session['username'])
    image = q1.image
    categories = Category.objects.all()
    companies = Company.objects.all()
    products = Product.objects.filter(available=True)
    if slug:
        company = get_object_or_404(Company, slug=slug)
        products = Product.objects.filter(company=company)
    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'companies': companies,
        'company': company,
        'image':image
    }
    return render(request, 'inventory/list.html', context)

def product_list(request, category_slug=None):
    q1 = Register.objects.get(email=request.session['username'])
    image = q1.image
    category = None
    company = None
    categories = Category.objects.all()
    companies = Company.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'companies': companies,
        'company': company,
        'image': image
    }
    return render(request, 'inventory/list.html', context)

def remove_stock(request, id, ty):
    q1 = Stocks.objects.get(id=id)
    return render(request, 'inventory/edit.html', context={'stock': q1, 'ty':ty})

def update_stock(request, id, ty):
    q1 = Stocks.objects.get(id=id)
    customer = request.session['username']
    customer = Register.objects.get(email=customer)
    product = q1.product
    quantity = request.POST['quantity']
    if ty == 'remove':
        q1.quantity -= int(quantity)
        opr = 'STOCKOUT'

    elif ty == 'add':
        q1.quantity += int(quantity)
        opr = 'STOCKIN'
    q1.save()
    q2 = LogInventory(user=customer, product=product, quantity=quantity, operation=opr)
    q2.save()
    return redirect('inventory:stock')