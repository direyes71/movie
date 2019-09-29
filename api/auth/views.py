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
    """ Token Login process
    """

    serializer_class = TokenObtainPairSerializer


class UserViewSet(GenericViewSet, CreateModelMixin):
    """ Manage users
    """

    permission_classes = (AllowAny,)
    serializer_class = NewUserSerializer
    queryset = User.objects.all()


class LogoutView(GenericAPIView):
    serializer_class = TokenVerifySerializer

    def post(self, request, *args):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
