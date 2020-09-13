from rest_framework import viewsets
from django.http import HttpResponse

from .serializers import CustomerSerializer
from .models import Customer


def index(request):
    return HttpResponse("<div style='text-align: center;margin-top: 100px;'><h1>Customer Demo Api</h1></div>")

class CustomerViewSet(viewsets.ModelViewSet):
    """ This class is used to perform CRUD operation over customer table"""

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    