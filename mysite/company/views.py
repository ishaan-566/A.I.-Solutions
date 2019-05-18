from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import *
from login.models import *
from django.shortcuts import render

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse(form.cleaned_data['your_name']+ str(form.cleaned_data['number']))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


def index(request):
    return HttpResponse("<h1>hello you are in company app")

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
    return render(request, 'company/product/list.html', context)


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
    return render(request, 'company/product/list.html', context)

def product_detail(request, id, slug):
    q1 = Register.objects.get(email=request.session['username'])
    image = q1.image
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    form = NameForm()
    quantity = [i for i in range(1, product.stock + 1)]
    context = {
        'product': product,
        'quantity': quantity,
        'form': form,
        'image':image
    }

    # return render(request, 'name.html', {'form': form})
    return render(request, 'company/product/detail.html', context)

def company_detail(request, slug):
    q1 = Register.objects.get(email=request.session['username'])
    image = q1.image
    company = get_object_or_404(Company, slug=slug)
    context = {
        'company': company,
        'image': image,
    }
    return render(request, 'company/product/cdetail.html', context)

def add_cart(request, id, slug):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['your_name']

    product = Product.objects.get(id=id)
    customer = request.session['username']
    customer = Register.objects.get(email=customer)
    cart = Cart(product=product, customer=customer, Quantity=quantity)
    cart.save()
    q2 = Cart.objects.filter(customer_id=customer.id).count()
    request.session['cart_items'] = q2
    return redirect('login:cart')