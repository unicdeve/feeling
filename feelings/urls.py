from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from django.views.generic import TemplateView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from users import urls as user_urls
from thoughts import urls as thoughts_urls
from groups import urls as group_urls

from users import routers as user_routers
from thoughts import routers as thought_routers

api_urlpatterns = [
    url(r'', include(user_routers.router.urls)),
    url(r'', include(thought_routers.router.urls)),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include(user_urls, namespace='users')),
    url(r'^thoughts/', include(thoughts_urls, namespace='thoughts')),
    url(r'^groups/', include(group_urls, namespace='groups')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^api/', include(api_urlpatterns)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),

    ]