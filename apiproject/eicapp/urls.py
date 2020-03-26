from django.urls import path, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from eicapp import views
from rest_framework import routers

from eicapp.views import UserViewSet, SectorViewSet, EmailViewSet, ChinesePageViewSet, NewsEventViewSet, IncentiveViewSet, CountryProfileViewSet, ServiceViewSet

router = routers.DefaultRouter()
# router.register(r'api/v1/users', UserViewSet)
router.register(r'api/v1/sectors', SectorViewSet)
router.register(r'api/v1/emails', EmailViewSet)
router.register(r'api/v1/chinesepages', ChinesePageViewSet)
router.register(r'api/v1/news', NewsEventViewSet)
router.register(r'api/v1/incentives', IncentiveViewSet)
router.register(r'api/v1/country-profiles', CountryProfileViewSet)
router.register(r'api/v1/services', ServiceViewSet)


urlpatterns = [
    path(r'', include(router.urls)),
    # path(r'api/', include('rest_framework.urls', namespace='rest_framework'))
]