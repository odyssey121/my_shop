from .cart import Cart

def cart(request):
    return {'cart': Cart(request),'test_var':100}
