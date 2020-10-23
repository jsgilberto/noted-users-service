from rest_framework import serializers
from rest_framework_simplejwt.tokens import UntypedToken
from noted_users.users.models import User
import jwt

class TokenVerifySerializer(serializers.Serializer):
    token = serializers.CharField()

    def validate(self, attrs):
        UntypedToken(attrs['token'])

        token = attrs["token"]

        # get user info from jwt
        decoded_payload = jwt.decode(token, None, None)
        user_id = decoded_payload.get('user_id', None)

        return { "user_id" : user_id }