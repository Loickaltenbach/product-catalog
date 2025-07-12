from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.http import JsonResponse
from django.contrib import messages
from decimal import Decimal
from .models import Product, Category


class ProductListView(ListView):
    """ListView for displaying products with category filtering"""
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True).select_related('category')
        category_id = self.request.GET.get('category')
        
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['selected_category'] = self.request.GET.get('category')
        return context


def product_detail(request, pk):
    """Detail view for a single product"""
    product = get_object_or_404(Product, pk=pk, is_active=True)
    return render(request, 'catalog/product_detail.html', {'product': product})


def add_to_cart(request, product_id):
    """Add a product to the session-based cart"""
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id, is_active=True)
        cart = request.session.get('cart', {})
        
        product_id_str = str(product_id)
        quantity = int(request.POST.get('quantity', 1))
        
        if product_id_str in cart:
            cart[product_id_str]['quantity'] += quantity
        else:
            cart[product_id_str] = {
                'name': product.name,
                'price': str(product.price),
                'quantity': quantity,
                'image': product.image.url if product.image else None
            }
        
        request.session['cart'] = cart
        request.session.modified = True
        
        messages.success(request, f'{product.name} added to cart!')
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            cart_count = sum(item['quantity'] for item in cart.values())
            return JsonResponse({'success': True, 'cart_count': cart_count})
        
        return redirect('catalog:cart_view')
    
    return redirect('catalog:product_list')


def cart_view(request):
    """Display cart contents with totals"""
    cart = request.session.get('cart', {})
    cart_items = []
    total = Decimal('0.00')
    
    for product_id, item in cart.items():
        item_total = Decimal(item['price']) * item['quantity']
        cart_items.append({
            'product_id': product_id,
            'name': item['name'],
            'price': Decimal(item['price']),
            'quantity': item['quantity'],
            'total': item_total,
            'image': item.get('image')
        })
        total += item_total
    
    context = {
        'cart_items': cart_items,
        'cart_total': total,
        'cart_count': sum(item['quantity'] for item in cart.values())
    }
    
    return render(request, 'catalog/cart.html', context)


def update_cart(request, product_id):
    """Update quantity of a product in the cart"""
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        product_id_str = str(product_id)
        quantity = int(request.POST.get('quantity', 1))
        
        if product_id_str in cart:
            if quantity > 0:
                cart[product_id_str]['quantity'] = quantity
            else:
                del cart[product_id_str]
            
            request.session['cart'] = cart
            request.session.modified = True
            messages.success(request, 'Cart updated successfully!')
        
        return redirect('catalog:cart_view')
    
    return redirect('catalog:cart_view')


def remove_from_cart(request, product_id):
    """Remove a product from the cart"""
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    
    if product_id_str in cart:
        product_name = cart[product_id_str]['name']
        del cart[product_id_str]
        request.session['cart'] = cart
        request.session.modified = True
        messages.success(request, f'{product_name} removed from cart!')
    
    return redirect('catalog:cart_view')


def clear_cart(request):
    """Clear all items from the cart"""
    if 'cart' in request.session:
        del request.session['cart']
        request.session.modified = True
        messages.success(request, 'Cart cleared successfully!')
    
    return redirect('catalog:cart_view')
