from django.conf.urls import url

from users.views import login_user, logout_user

urlpatterns = [
    url(r'login/', login_user),
    url(r'logout/', logout_user)
]