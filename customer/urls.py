from rest_framework import routers
from django.urls import path

from .views import CustomerViewSet

router = routers.DefaultRouter()
router.register('customer', CustomerViewSet, basename='customer')
urlpatterns = router.urls