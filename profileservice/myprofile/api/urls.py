from django.conf.urls import url

from myprofile.api.views import ProfileViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

router = SimpleRouter()
router.register(r'profiles', ProfileViewSet)

