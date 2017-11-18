from rest_framework import viewsets
from myprofile.models import Profile
from myprofile.api.serializers import ProfileSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

