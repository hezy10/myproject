from django.conf.urls import url,include
from rest_framework_jwt.views import obtain_jwt_token


from . import views


urlpatterns = [
  url(r'mobile/(?P<phone>\d{11})/$',views.PhoneCodeView.as_view())
  # url(r'mobile/(?P<phone>\d{11})/$',views.PhoneCodeView.as_view())
]
