from django.shortcuts import render,redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import OrderCreated
from django.urls import reverse

# Create your views here.
def OrderCreate(request):
    cart=Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,quantity=item['quantity'],product=item['product'],price=item['price'])
            cart.clear()
            #Ассинхроная отправка сообщений
            OrderCreated.delay(order.id)
            request.session['order_id']=order.id
            return redirect(reverse('payment:process'))
            
    form=OrderCreateForm
    return render(request,'orders/order/create.html',{'form':form})
