from rest_framework_simplejwt.views import TokenViewBase
from .serializers import TokenVerifySerializer


class TokenVerifyView(TokenViewBase):
    """
    Takes a token and indicates if it is valid.  This view provides no
    information about a token's fitness for a particular use.
    """
    serializer_class = TokenVerifySerializer


token_verify = TokenVerifyView.as_view()