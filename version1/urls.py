from django.conf import urls
from django.conf.urls import url
from .views import ShowConfigs

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Kashif''s API')


urlpatterns = [

    # PROD section
    # Host Endpoints
    urls.url(r'version1/show_config/', ShowConfigs.as_view({'get': 'ShowConfig'})),

    # Swagger Schema
    url(r'^$', schema_view)
    ]