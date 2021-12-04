from .models import Order
from rest_framework import serializers, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

import razorpay

# Serializers define the API representation.
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'txn_order_id', 'txn_oder_amnt', 'txn_pmnt_id', 'txn_signature']

# ViewSets define the view behavior.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(methods=['POST'], detail=False)
    def generate_order(self, request):
        client = razorpay.Client(auth=("rzp_test_RzqGUte2fyaI4Y", "CNZLzLiSXM8378e0RqRNaN73"))
        data = { "amount": 2500, "currency": "INR"}
        payment = client.order.create(data=data)
        print(payment)
        return Response(data=payment, status=status.HTTP_200_OK)
