from rest_framework import viewsets
from .serializers import CustomerSerializer
from .models import Customer

class CustomerViewSet(viewsets.ModelViewSet):
    """ This class is used to perform CRUD operation over customer table"""

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    