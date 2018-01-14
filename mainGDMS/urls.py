from django.conf.urls import url
from . import views
from django.contrib.auth.views import login


urlpatterns = [
	url(r'^browse/(?P<tableName>\w{1,50})$', views.browseTable, name = 'browseTable' ),
	url(r'^browse', views.browse, name = 'browse' ),
	url(r'^edit/(?P<whatToEdit>\w{1,50})$', views.edit, name='edit'),
	url(r'^tryremove/(?P<whatToRemove>\w{1,50})$', views.tryRemoveRecord, name='tryRemoveRecord'),
	url(r'^remove/(?P<whatToRemove>\w{1,50})$', views.removeRecord, name='removeRecord'),
	url(r'^get/(?P<whatToGet>\w{1,50})$', views.getData, name='getData'),
	url(r'^logout', views.showLogout, name = 'logout' ),
    url(r'^$', login, {'template_name': 'mainGDMS/login.html'} ,name = 'indexName' )
]