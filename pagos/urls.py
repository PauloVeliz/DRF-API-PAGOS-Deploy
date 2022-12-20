from rest_framework import routers
from django.urls import re_path,include

from versionedPagos.v1.router import api_urlpatterns as api_v1

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
            re_path(r'api/v1/',include(api_v1)),
            ]