from django.conf.urls import url
from . import views # . means import from current directory

app_name = 'tools'

urlpatterns = [
    url(r'^$', views.tools_list, name='list'),
]
