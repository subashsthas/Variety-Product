from django.test import TestCase, Client
from .views import *



# Create your tests here.


class Test(TestCase):

    def test_Price(self):
        prod = Product.objects.create(product_name="budget sheet", product_category="Management", product_rate=100.000)
        self.assertTrue(prod.TestPrice())

    def test_product_category(self):
        product_category = Product.objects.create(product_name="budget sheet", product_category="Management", product_rate=100.000)
        if product_category.product_category == "Management":
            self.assertTrue(product_category.TestProductCategory())
        elif product_category.product_category == "Science":
            self.assertFalse(product_category.TestProductCategory())

    def test_not_same_productName_and_productCategory(self):
        name_validation = Product.objects.create(product_name="Calculator", product_category="Extra",
                                                 product_rate=300.0000)
        self.assertTrue(name_validation.TestProductNameAndCategory())

    def test_details(self):
        desc = Product.objects.create(product_name="chartpaper", product_category="Extra",
                                      product_rate=10.0000,
                                      product_details="Chart paper for drawing, doing projects."
                                      )
        self.assertTrue(desc.TestProductDetails())
