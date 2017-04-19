from django.conf.urls import url
from django.contrib.auth import views as auth_views

from core import views

urlpatterns = [
    url(r'^$',views.index,name='core.views.index'),
    url(r'^login/$', auth_views.login, {'template_name': 'core/login.html'}, name='core.views.login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'core/logout.html'}, name='core.views.logout'),
    url(r'^signup/$', views.signup, name='core.views.signup'),
    url(r'^start/$', views.start, name='core.views.start'),
    url(r'^gallery/$', views.gallery, name='core.views.gallery'),
]
