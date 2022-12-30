from django.shortcuts import render
from .models import Product

# Create your views here.

def catalog_view(request):
    catalog = [
        Product(product_id=1, name='Sepapu Adidas', category='brand', price=100000, stock=20, description='Sepatu bagus'),
        Product(product_id=2, name='Tas Eiger', category='local', price=300000, stock=3, description='Tas bagus'),
        ]

    list_barang = Product.get_catalog()
    page_title = 'Catalog'
    context = {'catalog':list_barang, 'title':page_title}
    return render(request, 'catalog.html', context)