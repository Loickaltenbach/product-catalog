def cart_context(request):
    """
    Context processor to make cart information available in all templates
    """
    cart = request.session.get('cart', {})
    cart_count = sum(item['quantity'] for item in cart.values()) if cart else 0
    
    return {
        'cart_count': cart_count,
    }
