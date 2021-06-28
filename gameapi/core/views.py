from django.contrib.auth import authenticate
from django.conf import settings

from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView


@permission_classes([IsAuthenticated])
class HelloView(APIView):
    def get(self, request):
        content = {'message': 'Hello, world'}
        return Response(content)


@api_view(['POST'])
@permission_classes([AllowAny])
def get_tokens(request):

    username = request.data.get("username")
    email = request.data.get("email")

    user = authenticate(username=username, email=email)

    if user is not None:
        refresh_token = RefreshToken.for_user(user)

        return Response({
            'status': True,
            'message': 'Authenticate successful',
            'refresh': str(refresh_token),
            'access': str(refresh_token.access_token),
        })

    else:
        return Response({
            'message': 'Authenticate unsuccessful',
            'status': False
        })
