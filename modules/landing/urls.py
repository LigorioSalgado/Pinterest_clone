
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index,name="index"),
    url(r'^login/$', Login,name="login"),
    url(r'^signup/$', SignUp,name="signup"),

]
