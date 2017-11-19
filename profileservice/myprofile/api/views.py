from rest_framework import viewsets
from myprofile.models import Profile
from myprofile.api.serializers import ProfileSerializer
from rest_framework.authentication import (SessionAuthentication,
                                           BasicAuthentication,
                                           TokenAuthentication)
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)


class ProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

