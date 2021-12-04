# Routers provide an easy way of automatically determining the URL conf.
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .views import OrderViewSet

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]