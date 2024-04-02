from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView

from .views import CarroViewSets
from .views import UserViewSets

app_name = 'app'

urlpatterns_jwt = [
    path(
        'token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'token/verify/',
        TokenVerifyView.as_view(),
        name='token_verify'
    ),
]

router = DefaultRouter()
router.register('carro', CarroViewSets, basename='carro-api')
router.register('user', UserViewSets, basename='user-api')


urlpatterns = router.urls
urlpatterns += urlpatterns_jwt
