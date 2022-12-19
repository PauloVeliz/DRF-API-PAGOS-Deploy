from rest_framework import routers
from .api import PagosView

router = routers.DefaultRouter()
router.register(r'pagos',PagosView,'pagos')

urlpatterns = []

urlpatterns += router.urls
