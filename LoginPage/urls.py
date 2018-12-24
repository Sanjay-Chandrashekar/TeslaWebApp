from django.conf.urls import include, url

from LoginPage.views import LogIn

urlpatterns = [
    url('', LogIn.as_view(), name='index'),
]