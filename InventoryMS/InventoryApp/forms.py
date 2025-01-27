# Form to add product to inventory / database
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_id': 'Product ID',
            'product_name': 'Product Name',
            'product_category': 'Product Category',
            'product_sku': 'Product SKU',
            'product_price': 'Product Price',
            'product_quantity': 'Product Quantity',
            'product_weight': 'Product Weight',
            'product_color': 'Product Color',
            'product_size': 'Product Size',
            'product_supplier': 'Product Supplier',
            'product_description': 'Product Description',
            'product_image': 'Product Image'
        }
        widgets = {
            'product_id': forms.NumberInput(attrs={'placeholder': 'e.g. 1', 'class': 'form-control'}),  # Optional
            'product_name': forms.TextInput(attrs={'placeholder': 'e.g. Sented Candle', 'class': 'form-control'}),
            'product_category': forms.Select(attrs={'class': 'form-control'}),  # Dropdown for categories
            'product_sku': forms.TextInput(attrs={'placeholder': 'e.g. WA12345', 'class': 'form-control'}),
            'product_price': forms.NumberInput(attrs={'placeholder': 'e.g. 100.00', 'class': 'form-control'}),
            'product_quantity': forms.NumberInput(attrs={'placeholder': 'e.g. 100', 'class': 'form-control'}),
            'product_weight': forms.NumberInput(attrs={'placeholder': 'e.g. 1.00', 'class': 'form-control'}),
            'product_color': forms.TextInput(attrs={'placeholder': 'e.g. Light Blue', 'class': 'form-control'}),
            'product_size': forms.Select(attrs={'class': 'form-control'}),  # Dropdown for sizes
            'product_supplier': forms.TextInput(attrs={'placeholder': 'e.g. ABCorp China', 'class': 'form-control'}),
            'product_description': forms.Textarea(attrs={'placeholder': 'e.g. Scented white wax candle in a glass', 'class': 'form-control'}),
            'product_image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/png, image/jpeg'})  # Restrict file types
}
