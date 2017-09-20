import json

from django.http import HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authtoken.models import Token

from api.serializers import UserSerializer
from users.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')

        if pk == 'current':
            return self.request.user

        return super(UserViewSet, self).get_object()


@csrf_exempt
def api_token_auth_session(request):
    if not request.user.is_authenticated:
        return HttpResponse(
            json.dumps({'detail': 'Not logged in'}),
            content_type='application/json',
            status=status.HTTP_403_FORBIDDEN
        )

    token = request.user.auth_token
    if token is None:
        token = Token(user=request.user)
        token.save()

    return HttpResponse(
        json.dumps({'token': token.key}),
        content_type='application/json',
        status=status.HTTP_200_OK
    )
