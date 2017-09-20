from django.conf.urls import url, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.views import api_token_auth_session, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^api-token-auth-session/', api_token_auth_session),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url('^', include(router.urls))
]
