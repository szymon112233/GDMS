from django.conf.urls import url
from . import views
from django.contrib.auth.views import login


urlpatterns = [
	url(r'^browse/(?P<tableName>\w{1,50})$', views.browseTable, name = 'browseTable' ),
	url(r'^browse', views.browse, name = 'browse' ),
	url(r'^edit', views.edit, name = 'edit' ),
	url(r'^logout', views.showLogout, name = 'logout' ),
    url(r'^$', login, {'template_name': 'mainGDMS/login.html'} ,name = 'indexName' )
]