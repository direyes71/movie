from django.contrib.auth import get_user_model

from rest_framework import serializers


class NewUserSerializer(serializers.ModelSerializer):
    """ Serializer for new users
    """

    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'password',
            'age',
            'gender',
        )

    def create(self, validated_data):
        user = super(NewUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
