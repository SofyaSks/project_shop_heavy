from django.shortcuts import render, redirect
from django.urls import reverse
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST, request = request)
        if form.is_valid():
            order = form.save()
            for item in cart:
                discount_price = item['product'].sell_price()
                OrderItem.objects.create(order=order, product = item['product'], 
                                         price = item['price'], quantity = item['quantity'])
            cart.clear()
            request.session['order_id'] = order.id
            # return render(
            #     request,
            #     'order/created.html',
            #     {'order': order,
            #      'form': form}
            # )
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm(request = request)
    return render(
                request,
                'order/create.html',
                {'cart': cart,
                 'form': form}
            )

# 6 24 25