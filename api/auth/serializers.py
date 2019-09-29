from django.contrib.auth.models import User

from rest_framework import serializers


class NewUserSerializer(serializers.ModelSerializer):
    """ Serialzer for new users
    """

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )

    def create(self, validated_data):
        user = super(NewUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
