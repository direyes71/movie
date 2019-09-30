from django.conf.urls import url
from django.urls import include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView

from api.auth.views import AuthTokenLogin
from api.auth.views import LogoutView
from api.auth.views import UserViewSet


router = DefaultRouter()
router.register(r'sign-up', UserViewSet, base_name='user')


urlpatterns = [
    url('login-token/', AuthTokenLogin.as_view(), name='token_obtain_pair'),
    url('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    url('verify-token/', TokenVerifyView.as_view(), name='token_verify'),
    url('logout/', LogoutView.as_view(), name='logout'),

    url('', include(router.urls)),
]
