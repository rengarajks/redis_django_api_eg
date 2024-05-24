from rest_framework import serializers
from .models import Product_list

class prduct_serialize(serializers.ModelSerializer):
    class Meta:
        model=Product_list
        fields=('__all__')