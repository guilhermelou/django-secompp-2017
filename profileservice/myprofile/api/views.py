from rest_framework import viewsets, mixins
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User

from main.api.permissions import IsOwnerOrReadOnly
from myprofile.models import Profile, Heart
from myprofile.api.permissions import IsFromProfileOrReadOnly
from myprofile.api.serializers import (ProfileSerializer, UserSerializer,
                                       HeartSerializer)


class ProfileViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):

    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class HeartViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):

    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticatedOrReadOnly, IsFromProfileOrReadOnly)

    queryset = Heart.objects.all()
    serializer_class = HeartSerializer

    def create(self, request, *args, **kwargs):
        request.data['profile_from'] = request.user.profile.id
        return super(self.__class__, self).create(request, *args, **kwargs)
