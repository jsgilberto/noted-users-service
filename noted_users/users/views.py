from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.decorators import ( api_view, 
    authentication_classes, permission_classes )
from rest_framework.response import Response
from .models import User
from .permissions import IsUserOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly, IsAuthenticated)
    # authentication_classes = (TokenAuthentication, JWTAuthentication,)


class UserCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def sanity_check(request):
    """ View used to check API status without need of
        permissions nor authentication
    """
    return Response({"healthy": True}, status=200)