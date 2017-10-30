from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^browse', views.browse, name = 'browse' ),
	url(r'^edit', views.edit, name = 'edit' ),
    url(r'^$', views.index, name = 'indexName' )
]