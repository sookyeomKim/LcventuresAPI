from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api.views import ApiViewSet

router = routers.DefaultRouter()
router.register(r'', ApiViewSet, basename='inquiry')

urlpatterns = [
    path('inquiry', include(router.urls))
]
