from django.urls import include
from django.urls import path

from rest_framework.routers import DefaultRouter

from api.catalog.views import MovieViewSet


router = DefaultRouter()
router.register(r'movie', MovieViewSet, base_name='movie')

urlpatterns = [
    path('', include(router.urls)),
]
