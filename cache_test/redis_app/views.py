from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import prduct_serialize
from .models import Product_list
from django.shortcuts import get_object_or_404
import json
from django.core.cache import cache



class Products(APIView):
    def get(self,request):
        query_set=Product_list.objects.all()
        data=prduct_serialize(query_set,many=True)
        return Response(data.data)


class Product(APIView):
    def get(self,request,id):
        #1.Construct cache key for given details 
        cache_key = f'details_{id}'

        #2.Check if data is checked
        cached_details = cache.get(cache_key)

        if cached_details:
             print("data from redis")
             data=json.loads(cached_details)
             return Response(data)


        print("data from db")
        query_set=get_object_or_404(Product_list,pk=id)
        data=prduct_serialize(query_set).data
        cache.set(key=cache_key,value=json.dumps(data))
        return Response(data)
