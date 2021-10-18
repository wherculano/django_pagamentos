from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
from pages.views import ClientViewSet, BillsViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'client', ClientViewSet, basename='Client')
router.register(r'bills', BillsViewSet, basename='Bills')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls))
]
