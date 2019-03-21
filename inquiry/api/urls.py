from django.urls import path, include
from rest_framework import routers

from api.views import ApiViewSet

router = routers.DefaultRouter()
router.register(r'inquiry', ApiViewSet, basename='inquiry')

urlpatterns = [
    path('', include(router.urls))
]
