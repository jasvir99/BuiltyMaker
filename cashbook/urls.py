from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
from BuiltyMaker.cashbook.models import *
urlpatterns = patterns('BuiltyMaker.cashbook.views',
	(r'^$','index'),
)
