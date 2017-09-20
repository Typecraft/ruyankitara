
# Create your views here.
import requests
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response

from api.serializers import UserSerializer
from users.models import User


# Create your views here.
@api_view(['GET', 'POST'])
@renderer_classes((TemplateHTMLRenderer,))
def login_user(request):
    if request.user.is_authenticated:
        return redirect('/words')

    if request.method == 'GET':
        return Response(
            template_name='words/login.html'
        )

    username = request.data.get('username')
    password = request.data.get('password')

    response = requests.post('http://login.typecraft.org/login', data={
        'username': username, 'password': password
    })

    # Response expected to contain user information. If the user does not exist in the local database yet,
    # create it. If it doesn't exist remotely, redirect to signup with data
    if response.status_code == 200:
        response_data = response.json()  # Expected to contain a DRF-serialized version of a user
        username = response_data.get('username')
        user = User.objects.filter(username=username).first()

        if not user:
            serializer = UserSerializer(data=response_data, context={'request': request})
            if not serializer.is_valid():
                return Response({
                    'detail': 'Critical error, login server returned bad data.',
                    'source': response_data
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR, template_name='words/login.html')

            new_user = serializer.save()
            login(request, new_user)
            return redirect('/words')
        else:
            login(request, user)
            return redirect('/words')
    else:
        return Response(
            {'detail': 'Bad username or password', 'source': response.content},
            status=status.HTTP_403_FORBIDDEN,
            template_name='words/login.html'
        )


@api_view(['GET', 'POST'])
def logout_user(request):
    if 'next' in request.query_params or not request.is_ajax():
        response = Response(
            headers={'Location': request.query_params.get('next', '/')},
            status=status.HTTP_302_FOUND
        )
    else:
        response = Response(status=status.HTTP_200_OK)

    if not request.user.is_authenticated:
        return response

    logout(request)
    return response