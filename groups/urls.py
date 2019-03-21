from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^company/create/$', views.CompanyCreate.as_view(), name='company_create'),
]