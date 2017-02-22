from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$', views.post_list, name='post_list'),	#assigning a view called post_list to the URL
]