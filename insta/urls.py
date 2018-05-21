from django.conf.urls import url
from django.conf.urls.static import static
from . import views


urlpatterns=[
    url(r'^$',views.landing,name='landing'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^explore/$',views.explore,name='explore'),
]