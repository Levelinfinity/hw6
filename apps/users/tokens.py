from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserSerializer

def user_payload(user):
    return UserSerializer(user).data

def token_payload(user):
    token, _created = Token.objects.get_or_create(user=user)

    return {
        'auth': 'token',
        'token': token.key,
        'user': user_payload(user),
    }

def jwt_payload(user):
    refresh = RefreshToken.for_user(user)
    return {
        'auth_type': 'jwt',
        'access': str(refresh.access_token),
        'refresh':str(refresh),
        'user': user_payload(user),
    }
