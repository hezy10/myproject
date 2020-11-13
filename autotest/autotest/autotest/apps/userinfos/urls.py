from django.conf.urls import url,include
from rest_framework_jwt.views import obtain_jwt_token


from . import views


urlpatterns = [
   url(r'register/',views.RegisterView.as_view()),
   url(r'authorizations/',obtain_jwt_token),
   url(r'userinfo/',views.UserinfoView.as_view()),
   # url(r'changing/',)
]
