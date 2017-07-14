
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index,name="index"),
    url(r'^login/$', Login,name="login"),
    url(r'^signup/$', SignUp,name="signup"),
    url(r'^logout/$', Logout,name="logout"),
    url(r'^upload/$', UploadImage,name="imagen"),
    url(r'^profile/$', Profile ,name="profile"),
    url(r'^endpoint/images/$', ImagesEndpoint ,name="profile"),
    url(r'^endpoint/images/upload/$', ImagesEndpointUpload ,name="profile"),

]
