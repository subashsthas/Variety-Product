from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json 
from django.views.decorators.csrf import csrf_exempt

from shop.forms import CrudForm
from shop.models import Product

# restapi get all model data
def show_all_data(request):
	product = Product.objects.all()
	print(type(product))
	dict_type = {"Product": list(product.values("product_name", "product_category", "product_details", "product_rate"))}
	return JsonResponse(dict_type)

# restapi get specific model data by id
def get_data_json(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == "GET":
        return JsonResponse({"Product Name": product.product_name, "Product Category": product.product_category, "Product Details": product.product_details, "Product Rate": product.product_rate})

# restapi update specific model data by id
@csrf_exempt
def update_data_json(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == "GET":
        return JsonResponse({"Product Name": product.product_name, "Product Category": product.product_category, "Product Details": product.product_details, "Product Rate": product.product_rate})
    else:
        json_body = request.body.decode('utf-8')
        json_data = json.loads(json_body)
        product.product_name = json_data['product_name']
        product.product_category = json_data['product_category']
        product.product_details = json_data['product_details']
        product.product_rate = json_data['product_rate']
        product.save()
        return JsonResponse("Updated !", safe=False)

# restapi delete specific model data by id
@csrf_exempt
def delete_data_json(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == "GET":
        return JsonResponse({"Product Name": product.product_name, "Product Category": product.product_category, "Product Details": product.product_details, "Product Rate": product.product_rate})
    else:
        product.delete()
        return JsonResponse("Deleted !", safe=False)

# restapi post model data
@csrf_exempt
def post_data_json(request):
    if request.method == "POST":
        product = Product()
        json_body = request.body.decode('utf-8')
        json_data = json.loads(json_body)
        product.product_name = json_data['product_name']
        product.product_category = json_data['product_category']
        product.product_details = json_data['product_details']
        product.product_rate = json_data['product_rate']
        product.save()
        return JsonResponse("Uploaded !", safe=False)

