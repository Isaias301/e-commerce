from django.conf.urls import url
from news.views import teste, index, get, post, products

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^post/$', post, name='post'),
    url(r'^get/$', get, name='get'),
    url('user_list_all', teste, name='user_list_all'),
    url(r'^products/$', products, name='products'),
]