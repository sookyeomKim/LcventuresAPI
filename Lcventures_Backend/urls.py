from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from consult.views import ConsultViewSet

router = routers.DefaultRouter()
router.register('consult', ConsultViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
