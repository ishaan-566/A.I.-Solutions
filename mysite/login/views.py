from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from inventory.models import *
from .forms import RegisterForm, LoginForm
from django.conf import settings
import stripe


class HomeView(generic.TemplateView):
    template_name = "login/login.html"

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name)


class LoginView(generic.TemplateView):
    model = Register
    template_name = "login/login.html"

    form = LoginForm()

    def get(self, request):
        if request.session.has_key('username'):
            username = request.session['username']
            q1 = Register.objects.get(email=username)
            q2 = Cart.objects.filter(customer_id=q1.id).count()
            image = q1.image
            request.session['cart_items'] = q2
            return render(request, 'company/product/list.html', {"username": username, 'image': image})
        return render(request, self.template_name, context={'form': self.form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():

            # username = request.POST['Username']
            # password = request.POST['password']
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                q1 = Register.objects.get(email=username)
            except:
                return render(request, self.template_name, {'error': "User did not exist", 'form': form})
            request.session['username'] = username
            if password == q1.password:
                q2 = Cart.objects.filter(customer_id=q1.id).count()
                request.session['cart_items'] = q2
                return render(request, 'company/product/list.html', {"username": username})
            else:
                msg = "Please enter correct Password"
                return render(request, self.template_name, {'error': msg, 'form': form})


class RegisterView(generic.TemplateView):
    model = Register
    template_name = "login/register.html"

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            repassword = form.cleaned_data['repassword']
            phone_no = form.cleaned_data['phone_no']
            img = form.cleaned_data['img']
            q1 = None
            try:
                q1 = Register.objects.filter(email=email).get()
            except:
                pass

            if q1 is not None:
                msg = "User already exist....."
                args = {'form': form, 'error': msg}
                return render(request, self.template_name, args)
            else:
                if password == repassword:
                    Reg = Register(Fullname=name, email=email, password=password, phone=phone_no, image=img)
                    Reg.save()
                    home = HomeView()
                    return redirect('login:login')
                else:
                    msg = "Please enter correct password"
                    args = {'form': form, 'error': msg}
                    return render(request, self.template_name, args)
        else:
            return HttpResponse("Error")


def reg(request):
    return HttpResponse("hello")


def logout(request):
    request.session.flush()
    return redirect("login:login")


def cart(request):
    q1 = Register.objects.get(email=request.session['username'])
    q2 = Cart.objects.filter(customer_id=q1.id)
    image = q1.image
    context = {
        'item': q2,
        'image': image
    }
    return render(request, 'login/cart.html', context=context)


def update(request, id):
    q1 = Cart.objects.get(id=id)
    q1.Quantity = 10
    q1.save()
    return redirect("login:cart")


def delete(request, id):
    q1 = Cart.objects.get(id=id)
    q1.delete()
    request.session['cart_items'] -= 1
    return redirect("login:cart")


def home(request):
    q1 = Bill.objects.filter(name=request.session['username'])
    user = Register.objects.get(email=request.session['username'])
    a = []
    b = LogInventory.objects.filter(user= user)
    for i in q1:
        q2 = Log.objects.filter(bill_id=i.id)
        a+=[j for j in q2]
    return render(request, 'profile1.html', {'data': a, 'user': user, 'data1':b})


def checkout(request):
    q1 = Register.objects.get(email=request.session['username'])
    q2 = Cart.objects.filter(customer_id=q1.id)
    ob = Bill(name=request.session['username'])
    ob.save()
    request.session['number'] = ob.id
    total = 0
    for i in q2:
        total += i.Quantity * i.product.price
        q = Log(bill_id=ob.id, product=i.product, Quantity=i.Quantity)
        q.save()
        i.delete()
    request.session['total'] = total*100
    request.session['cart_items'] = 0
    return redirect('login:confirm')

def confirm(request):
    context = {'key': settings.STRIPE_PUBLISHABLE_KEY, 'amount': request.session['total']}
    return render(request, 'confirm.html', context)

def charge(request):
    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        charge = stripe.Charge.create(
            amount=int(request.session['total']),
            currency='inr',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return redirect('login:bill')

def bill(request):
    id = request.session['number']
    bill = Bill.objects.get(id=id)
    q1 = Log.objects.filter(bill_id=id)
    q2 = Register.objects.get(email=request.session['username'])
    context = {
        'items': q1,
        'invoice': id,
        'name': q2.Fullname,
        'email': q2.email,
        'phone': q2.phone,
        'date': bill.date,
        'total': request.session['total']/100,
    }
    return render(request, 'invoice.html', context=context)
