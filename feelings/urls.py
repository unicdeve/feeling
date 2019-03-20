from django.conf.urls import url, include
from django.contrib import admin

from django.views.generic import TemplateView

from users import urls as user_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include(user_urls, namespace='users')),
    url(r'$', TemplateView.as_view(template_name='index.html'), name='home'),

]