# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^entrar/$', login, name='entrar'),
    url(r'^sair/$', logout, {'next_page': 'entrar'}, name='sair'),
]