from django.conf.urls import url

from myprofile.api.views import ProfileViewSet, UserViewSet, HeartViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

router = SimpleRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'users', UserViewSet)
router.register(r'hearts', HeartViewSet)

