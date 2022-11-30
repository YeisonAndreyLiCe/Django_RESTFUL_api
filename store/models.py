from django.db import models
from django.utils import timezone

class Product(models.Model):
    DISCOUNT_RATE = 0.01

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    sale_start = models.DateTimeField(blank=True, null=True, default=None)
    sale_end = models.DateTimeField(blank=True, null=True, default=None)
    photo = models.ImageField(upload_to='products', blank=True, null=True, default=None)

    def is_on_sale(self):
        now = timezone.now()
        if self.sale_start:
            if self.sale_end:
                return self.sale_start <= now <= self.sale_end
            else:
                return self.sale_start <= now
        return False

    def get_rounded_price(self):
        return round(self.price, 2)

    def current_price(self):
        if self.is_on_sale():
            discounted_price = self.price*(1 - self.DISCOUNT_RATE)
            return round(discounted_price, 2)
        return self.get_rounded_price()

    def __rep__(self):
        return f"< Product object {self.id}, {self.name}>"

    def __str__(self):
        return self.name


class ShoppingCart(models.Model):
    TAX_RATE = 0.13

    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def subtotal(self):
        amount = 0
        for item in self.shopping_cart_items:
            amount += item.quantity * item.product.current_price()
        return round(amount, 2)

    def taxes(self):
        return round(self.subtotal() * self.TAX_RATE, 2)

    def total(self):
        return round(self.subtotal() + self.taxes(), 2)

    def __repr__(self):
        name = self.name or "[Guest]"
        address = self.address or "[No address]"
        return f"<ShoppingCart object {self.id}, {name}, {address}>"

    def __str__(self):
        return self.name or "Guest"
    
class ShoppingCartItem(models.Model):
    shopping_cart = models.ForeignKey(ShoppingCart, related_name="items", related_query_name="item", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="+", on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __repr__(self):
        return f"<ShoppingCartItem object {self.id}, {self.product.name}, {self.quantity} * {self.product.name}>"

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    def total(self):
        return round(self.product.current_price() * self.quantity, 2)