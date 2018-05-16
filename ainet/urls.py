# https://docs.djangoproject.com/en/1.11/topics/http/urls/
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from decouple import config

urlpatterns = [
                  url(r'^admin/',
                      admin.site.urls),
                  url(r'^', include('main.urls')
                      ),
                  url(r'^customers/', include('customers.urls')
                      ),
                  url(r'^service/', include('service.urls')
                      ),
                  # reports list
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if config('DEBUG', default=True, cast=bool):
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
