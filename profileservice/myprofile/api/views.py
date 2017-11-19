from rest_framework import viewsets
from myprofile.models import Profile, Heart
from myprofile.api.permissions import IsFromProfileOrReadOnly
from myprofile.api.serializers import (ProfileSerializer, UserSerializer,
                                       HeartSerializer)

from rest_framework.authentication import (SessionAuthentication,
                                           BasicAuthentication,
                                           TokenAuthentication)

from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from main.api.permissions import IsOwnerOrReadOnly
from rest_framework import mixins
from django.contrib.auth.models import User


class ProfileViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):

    authentication_classes = (SessionAuthentication, TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

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

    authentication_classes = (SessionAuthentication, TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly, IsFromProfileOrReadOnly,)

    queryset = Heart.objects.all()
    serializer_class = HeartSerializer

    def create(self, request, *args, **kwargs):
        request.data['profile_from'] = request.user.profile.id
        return super(self.__class__, self).create(request, *args, **kwargs)

