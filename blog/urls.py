from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$', views.post_list, name='post_list'),	#assigning a view called post_list to the URL
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail') #^post/ means the URL shall begin with post and a "/".

	#(?P<pk>\d+) means that django will take everything you put after the "post/" into a variable called pk as we declared on 
	# post_list.html. "\d" means it must be a digit and "+" means it shall be one or more digit. not-valid = azad/blog/post//
	#valid = azad/blog/post/123/ . /$ means it must end with a '/'. $ means end, ^ means begin
]