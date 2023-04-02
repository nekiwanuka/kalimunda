from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
#we are going to include model so that view can use those models
from .models import Product, Sale
#We are going to include our filter so that can be  used our by views
from .filters import Product_filter

# Create your views here.

# Including our models forms created in the forms file
from .forms import AddForm, SaleForm

@login_required
def index(request):
    products = Product.objects.all().order_by('-id')
    products_filter = Product_filter(request.GET, queryset = products)
    products = products_filter.qs 
    return render(request, 'products/index.html', {'products':products,'products_filter': products_filter})

@login_required
def home(request):
    return render(request, 'products/aboutDrkalimunda.html')

# create a view for the product details identified by ID
# @login_required is a decorator, it comes before the function, it is excuted before the other proceeding function.

@login_required
def product_details(request, product_id):
    product = Product.objects.get(id = product_id)
    return render(request,'products/product_detail.html',{'product': product})

@login_required
def issue_item(request, pk):
    issued_item = Product.objects.get(id = pk)
    sales_form = SaleForm(request.POST)
    
    if request.method == 'POST':
        #checks if the input is as it set to functions or to the purpose
        if sales_form.is_valid():
            new_sale = sales_form.save(commit = False)
            new_sale.item = issued_item
            new_sale.unit_price = issued_item.unit_price
            new_sale.save()
            # To keep track of the stock remaining after sales
            issued_quantity = int(request.POST['quantity'])
            issued_item.total_quantity -= issued_quantity
            issued_item.save()
            print(issued_item.item_name)
            print(request.POST['quantity'])
            print(issued_item.total_quantity)
            return redirect('receipt')
    return render(request, 'products/issue_item.html', {'sales_form':sales_form})


@login_required
def receipt(request):
    sales = Sale.objects.all().order_by('id')
    return render (request, 'products/receipt.html', {'sales':sales})  
            

@login_required
def add_to_stock(request, pk):
    pass
