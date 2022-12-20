from rest_framework.routers import DefaultRouter
from .api import ExpiredPaymentViewSet
router=DefaultRouter()

router.register(r"expired-payments",ExpiredPaymentViewSet,basename="expired-payments")

urlpatterns = router.urls
