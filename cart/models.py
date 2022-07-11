from django.db import models
from shop.models import  *
# Create your models here.
class cart(models.Model):
    cart_id=models.CharField(max_length=170,unique=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class item(models.Model):
    prodct=models.ForeignKey(product,on_delete=models.CASCADE)
    cart=models.ForeignKey(cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)
    def __str__(self):
        return str(self.prodct)

    def total(self):
        return self.prodct.price*self.quantity