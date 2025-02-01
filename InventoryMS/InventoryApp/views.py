from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

# Create your views here.

# CRUD  - Create, Read, Update, Delete

# Home view
def home_view(request):
    return render(request, 'inventoryApp/home.html')

# Create view
def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product_sku = form.cleaned_data['product_sku']
            
            # Check if a product with the same SKU already exists
            if Product.objects.filter(product_sku=product_sku).exists():
                form.add_error('product_sku', 'A product with this SKU already exists.')
            else:
                form.save()
                return redirect('product_list')  # Redirect to product list after saving

    else:
        form = ProductForm()
    
    return render(request, 'InventoryApp/product_form.html', {'form': form})


# Read view
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'inventoryApp/product_list.html', {'products': products})

# Update view
def product_update_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            # If no new image is uploaded, keep the old image
            if not request.FILES.get('product_image'):
                form.instance.product_image = product.product_image
            form.save()
            return redirect('product_list')

    return render(request, 'inventoryApp/product_form.html', {'form': form})


# Delete view
def product_delete_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'inventoryApp/product_confirm_delete.html', {'product': product})