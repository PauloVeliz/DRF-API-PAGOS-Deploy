from rest_framework import routers
from .api import LoginView,SignUpView,GetUsers
from django.urls import path
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


router = routers.DefaultRouter()
router.register('',GetUsers)

#router.register('', UserMixins, 'users')
#urlpatterns = router.urls
urlpatterns=[
    #path("", UserMixins.as_view(), name="mixins")
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt_create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),
]

urlpatterns += router.urls
# router = CustomRouter()
# router.register('', UserViewSet,'users')
# urlpatterns = router.urls