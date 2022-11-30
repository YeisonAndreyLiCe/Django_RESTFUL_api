from rest_framework import serializers
from store.models import Product, ShoppingCartItem

class CartItemSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(min_value=1, max_value=100)
    class Meta:
        model = ShoppingCartItem
        fields = ('product', 'quantity')

class ProductSerializer(serializers.ModelSerializer):
    is_on_sale = serializers.BooleanField(read_only=True)
    current_price = serializers.FloatField(read_only=True)
    description = serializers.CharField(min_length=2, max_length=200)
    cart_items = serializers.SerializerMethodField()
    #price = serializers.FloatField(min_value=0.01, max_value=100000)
    price = serializers.DecimalField(min_value=0.01, max_value=100000, max_digits=None, decimal_places=2)
    """ sale_start = serializers.DateTimeField(
        required=False, 
        input_formats=['%I:%M %p %d %B %Y', ], format=None, allow_null=True,
        help_text='Accepted Format is: 12:00 PM 31 December 2020',
        style={'input_type': 'text', 'placeholder': '15:00 PM 31 December 2020'},
    )
    sale_end = serializers.DateTimeField(
        required=False, 
        input_formats=['%I:%M %p %d %B %Y'], format=None, allow_null=True,
        help_text='Accepted Format is: 12:00 PM 31 December 2020',
        style={'input_type': 'text', 'placeholder': '13:00 PM 31 December 2020'}
    ) """
    photo = serializers.ImageField(default=None)
    warranty = serializers.FileField(write_only=True, default=None)
        
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'sale_start', 'sale_end', 'is_on_sale', 'current_price', 'cart_items', 'photo', 'warranty')

    def get_cart_items(self, obj):
        cart_items = ShoppingCartItem.objects.filter(product=obj)
        return CartItemSerializer(cart_items, many=True).data

    def update(self,instance,validated_data):
        if validated_data.get('warranty', None):
            instance.description += '\n\nWarranty: ' + validated_data['warranty'].read().decode('utf-8')
        return super().update(instance, validated_data)

    def create(self,validated_data):
        validated_data.pop('warranty')
        return Product.objects.create(**validated_data)


class ProductStatSerializer(serializers.Serializer):
    stats = serializers.DictField(
        child=serializers.ListField(
            child=serializers.IntegerField(),
        ),
    )