from rest_framework.routers import DefaultRouter, SimpleRouter

from myprofile.api.views import ProfileViewSet, UserViewSet, HeartViewSet


router = SimpleRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'users', UserViewSet)
router.register(r'hearts', HeartViewSet)

