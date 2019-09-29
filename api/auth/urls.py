from django.urls import include
from django.urls import path


from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView

from api.auth.views import AuthTokenLogin
from api.auth.views import LogoutView
from api.auth.views import UserViewSet


router = DefaultRouter()
router.register(r'user', UserViewSet, base_name='user')


urlpatterns = [
    path('login-token/', AuthTokenLogin.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify-token/', TokenVerifyView.as_view(), name='token_verify'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('', include(router.urls)),
]
