from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$',views.Home.as_view(),name="main"),
	url(r'^(?P<id>[0-9]+)/$',views.DetailView.as_view(),name='detalle')
]