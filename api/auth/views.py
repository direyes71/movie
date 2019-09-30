from django.contrib.auth import logout
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.serializers import TokenVerifySerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from api.auth.serializers import NewUserSerializer


class AuthTokenLogin(TokenObtainPairView):
    """ Takes a set of user credentials and returns an access and refresh JSON web
        token pair to prove the authentication of those credentials.

        Request: {
            "username": "test2",
            "password": "test"
        }
        Response: {JWT_AUTHENTICATION}
    """

    serializer_class = TokenObtainPairSerializer


class UserViewSet(GenericViewSet, CreateModelMixin):
    """ Signs up users
    """

    permission_classes = (AllowAny,)
    serializer_class = NewUserSerializer
    queryset = User.objects.all()


class LogoutView(GenericAPIView):
    """ Unvalidate Token for user
    """

    serializer_class = TokenVerifySerializer

    def post(self, request, *args):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
