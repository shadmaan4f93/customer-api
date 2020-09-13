import uuid
import json
from django.db import models
from django.utils import timezone

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=32, unique=True)
    phone =  models.CharField(max_length=16, unique=True)
    address = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)
   
    def __str__(self):
        return json.dumps({
            "id" : str(self.id),
            "name" : self.name,
            "email" : self.email
        })