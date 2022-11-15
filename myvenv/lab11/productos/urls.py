from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^productos/$', views.producto_list),
    re_path(r'^productos/(?P<pk>[0-9]+)/$', views.producto_detail),
]
