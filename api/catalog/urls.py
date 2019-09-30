from django.conf.urls import url
from django.urls import include

from rest_framework.routers import DefaultRouter

from api.catalog.views import MovieViewSet


router = DefaultRouter()
router.register(r'movie', MovieViewSet, base_name='movie')

urlpatterns = [
    url('', include(router.urls)),
]
