from rest_framework import generics, permissions
from .models import Customer
from .serializers import CustomerSerializer


class CustomerCreateView(generics.CreateAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    

