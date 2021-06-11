from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to="shop/images", default="")
    product_category = models.CharField(max_length=50)
    unit_Of_Product = models.CharField(max_length=25)
    product_rate = models.DecimalField(decimal_places=4, max_digits=50)
    product_details = models.TextField()

    def __str__(self):
        return self.product_name

    def TestPrice(self):
        return (self.product_rate > 000.0000)

    def TestProductCategory(self):
        return (self.product_category == "Management") or (self.product_category == "Science") or (self.product_category == "Extra")

    def TestProductNameAndCategory(self):
        return (self.product_name != self.product_category)

    def TestProductDetails(self):
        return (len(self.product_details) > 10)


class order(models.Model):
    products = models.OneToOneField(Product, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.products.product_name


class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    items = models.ManyToManyField(order)
    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.products.product_rate for item in self.items.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.user)



class Customer(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    customer_shopPic = models.ImageField(upload_to="shop/images/shop picture", default="")
    customer_shopName = models.CharField(max_length=100)
    customer_Pan = models.IntegerField()
    customer_address = models.CharField(max_length=100)
    customer_district = models.CharField(max_length=100)
    customer_proporator = models.CharField(max_length=100)
    customer_proporatorMobile = models.IntegerField()
    customer_contactPerson = models.CharField(max_length=100)
    customer_contactPersonMobile = models.IntegerField()
    customer_shopNumber = models.IntegerField()
    customer_residentPhone = models.IntegerField()
    customer_Transportation = models.CharField(max_length=100)


    def __str__(self):
        return self.customer_shopName

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.TextField(max_length=500, default="")


    def __str__(self):
        return self.name

