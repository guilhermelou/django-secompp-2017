from rest_framework import serializers
from myprofile.models import Profile, Message, Rate, Heart
from django.db.models import Avg

class ProfileSerializer(serializers.ModelSerializer):
    heart_count = serializers.SerializerMethodField()
    rate_average = serializers.SerializerMethodField()
    messages_count = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('id', 'job', 'city', 'heart_count', 'rate_average',
                  'messages_count', )

    def get_heart_count(self, obj):
        return Heart.objects.filter(profile_to=obj).count()

    def get_rate_average(self, obj):
        return Rate.objects.filter(profile_to=obj).aggregate(Avg('rate'))["rate__avg"]

    def get_messages_count(self, obj):
        return Message.objects.filter(profile_to=obj).count()

