from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import *
from .forms import CustomerForm, NewForm, CrudForm, ContactForm
from .models import Customer
from .models import Product, Contact, cart
from math import ceil
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.core.paginator import Paginator
from django.contrib.auth.models import User


def index(request):
    allProducts = []
    cateprods = Product.objects.values('product_category', 'product_id')
    cates = {item['product_category'] for item in cateprods}
    for cate in cates:
        prodf = Product.objects.filter(product_category=cate)
        n = len(prodf)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProducts.append([prodf, range(1, nSlides), nSlides])
    params = {'allProducts': allProducts}
    return render(request, 'main/index.html', params)


def update_customer(request, pk=None):
    instance = get_object_or_404(Customer, id=pk)
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('main:accounts')
    return render(request, "main/info.html", {"form": form})


# search function
def get_data_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        products = Product.objects.filter(
            Q(product_category__icontains=q) |
            Q(product_name__icontains=q)
        ).distinct()

        for product in products:
            queryset.append(product)
    return list(set(queryset))


# register
def register(request):
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:info")
    else:
        form = NewForm()
    return render(request, "main/register.html", {"form": form})


# add more details about shop or user
def info(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("main:login")

        else:
            form = CustomerForm()
    return render(request, "main/info.html", {"form": form})


# login
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'invalid credentials')
    form = AuthenticationForm()
    return render(request, 'main/login.html', {"form": form})


# logout
def user_logout(request):
    logout(request)
    return redirect('/')


# contactus
def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("main:contact")
        else:
            form = CustomerForm()
    return render(request, "main/contact.html", {"form": form})


def about(request):
    return render(request, 'main/about.html')


def accounts(request):
    return render(request, 'main/accounts.html')


def product_list(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 5)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        products = paginator.page(page)
    except(EmptyPage, InvalidPade):
        products = paginator.page(paginator.num_pages)

    return render(request, "main/product_list.html", {"products": products})


def delete_product(request, pk):
    product = Product.objects.get(pk=pk)  ##get ma pk vanney attribute
    product.delete()
    return redirect('main:product_list')


def add_to_cart(request, atc):
    product = Product.objects.get(pk=atc)  ##get ma pk vanney attribute
    cart = Cart.objects.get()
    cart.save()
    return redirect('main:index')


def crud(request):
    form = CrudForm()
    if request.method == "POST":
        form = CrudForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("main:crud")

        else:
            form = CrudForm()
    return render(request, 'main/crud.html', {"form": form})


def productView(request, product_id):
    # Fetch the product using the id
    product = Product.objects.filter(product_id=product_id)
    return render(request, 'main/prodView.html', {'product': product[0]})


def cart(request):
    return HttpResponse("This will be available after version 2.0")


def pagination(request, pageNo):
    get_all = Product.objects.all()
    if request.method == "GET":
        if pageNo == 1:
            pageNo = 0
            count = 0
            for i in range(8):
                try:
                    if get_all.get(id=i + 1) is not None:
                        count = count + 1
                    else:
                        break
                except:
                    pass
            get_spec = get_all[pageNo:count]
            return render(request, 'main/product_list.html', {'product': get_spec})
        else:
            count = 0
            i = (pageNo - 1) * 8
            for i in range(pageNo * 8):
                try:
                    if get_all.get(id=i + 1) is not None:
                        count = i + 1
                    else:
                        break
                except:
                    pass
            get_spec = get_all[(pageNo - 1) * 8:count]
            return render(request, 'main/product_list.html', {'product': get_spec})
