from django.conf.urls import url
from django.urls import include


urlpatterns = [
    url('auth/', include(('api.auth.urls', 'api.auth'), namespace='api_auth')),
    url('catalog/', include(('api.catalog.urls', 'api.catalog'), namespace='api_catalog')),
]
