from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Products
from .models import Categories
from .models import Provider
import json


# Create your views here.

class ProductsView(View):

  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
      return super().dispatch(request, *args, **kwargs)

  def get(self, request, prod_id=0):
    if (prod_id>0):
      productsList = list(Products.objects.filter(prod_id = prod_id).values())
      if len(productsList) > 0:
        product=productsList[0]
        data={'message':'Succes', 'products':product}
      else:
        data={'message':'Product not found...'}
      return JsonResponse(data)
    else:
      productsList = list(Products.objects.values())
      if len(productsList) > 0:
        data={'message':'Succes', 'products':productsList}
      else:
        data={'message':'Products not found...'}
      return JsonResponse(data)

  def post(self, request):
    #print(request.body)
    jd=json.loads(request.body)
    #print(jd)
    Products.objects.create(prod_description=jd['prod_description'], prod_unit_price=jd['prod_unit_price'], prod_stock=jd['prod_stock'])
    data={'message':'Succes'}
    return JsonResponse(data)

  def put(self, request, prod_id):
    jd=json.loads(request.body)
    productsList = list(Products.objects.filter(prod_id = prod_id).values())
    if len(productsList) > 0:
      product= Products.objects.get(prod_id = prod_id)
      product.prod_description=jd['prod_description']
      product.prod_unit_price=jd['prod_unit_price']
      product.prod_stock=jd['prod_stock']
      # product.cat_id=jd['cat_id']
      # product.prov_id=jd['prov_id']
      # product.prod_datetime_ingress=jd['prod_datetime_ingress']
      product.save()
      data={'message':'Succes'}
    else:
      data={'message':'Product not found...'}
    return JsonResponse(data)



  def delete(self, request, prod_id):
    productsList = list(Products.objects.filter(prod_id = prod_id).values())
    if len(productsList) > 0:
      Products.objects.filter(prod_id = prod_id).delete()
      data={'message':'Succes'}
    else:
      data={'message':'Product not found...'}
    return JsonResponse(data)

class CategoriesView(View):
  def get(self, request,):
    categoriesList = list(Categories.objects.values())
    if len(categoriesList) > 0:
      data={'message':'Succes', 'categories':categoriesList}
    else:
      data={'message':'Categories not found...'}
    return JsonResponse(data)

class ProviderView(View):
  def get(self, request,):
    providerList = list(Provider.objects.values())
    if len(providerList) > 0:
      data={'message':'Succes', 'Providers':providerList}
    else:
      data={'message':'Providers not found...'}
    return JsonResponse(data)

