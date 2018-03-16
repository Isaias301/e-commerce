from django.conf.urls import url
from app.core.views import index, product, products_list, contact

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^produto/$', product, name='produto'),
    url(r'^produtos/$', products_list, name='produtos'),
    url(r'^contato/$', contact, name='contato'),
]