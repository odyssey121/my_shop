from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart:
    def __init__ (self,request):
        self.session = request.session #получаем конкретную сессию из запроса
        cart=self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart=self.session[settings.CART_SESSION_ID]={}
        self.cart=cart
#Добавление товаров в корзину или обновление количества товаров
    def add(self,product,quantity=1,update_quantity=False):
        product_id=str(product.id)
        if product_id not in self.cart:
            self.cart[product_id]={'quantity':0,'price':str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity']=quantity
        else:
            self.cart[product_id]['quantity']+=int(quantity)
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID]=self.cart
        self.session.modified=True  #указываем что сессия изменена

    def remove(self,product):
        product_id=str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    def __iter__(self):
        product_ids=self.cart.keys()
        products=Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product']=product
        for item in self.cart.values():
            item['price']=Decimal(item['price'])
            item['total_price']=item['price']*item['quantity']
            yield item #возвращается сериализуемый словарь



    def clean(self):
        del self.session[CART_SESSION_ID]
        self.session.modified=True

    def get_total_price(self):
        return sum(Decimal(item.price)*item['quantity'] for item in self.cart.values())
