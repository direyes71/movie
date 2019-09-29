from django.urls import include
from django.urls import path


urlpatterns = [
    path('auth/', include(('api.auth.urls', 'api.auth'), namespace='api_auth')),
    path('catalog/', include(('api.catalog.urls', 'api.catalog'), namespace='api_catalog')),
]
