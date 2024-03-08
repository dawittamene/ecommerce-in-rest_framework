from rest_framework import serializers
from storeapp.models import *



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id','title','slug']  
        
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','description','discount','price','category','slug','inventory','top_deal','flash_sales']
    category = CategorySerializer()   
        
       