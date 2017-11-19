from rest_framework import serializers
from myprofile.models import Profile, Message, Rate, Heart
from django.db.models import Avg
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    heart_count = serializers.SerializerMethodField()
    rate_average = serializers.SerializerMethodField()
    messages_count = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('id', 'job', 'city', 'heart_count', 'rate_average',
                  'messages_count',)
        read_only_fields = ('user',)

    def get_heart_count(self, obj):
        return Heart.objects.filter(profile_to=obj).count()

    def get_rate_average(self, obj):
        return Rate.objects.filter(
			     profile_to=obj).aggregate(Avg('rate'))["rate__avg"]

    def get_messages_count(self, obj):
        return Message.objects.filter(profile_to=obj).count()


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'profile')

    def create(self, validated_data):
		print validated_data
		profile_data = validated_data.pop('profile')
		user = User.objects.create(**validated_data)
		user.set_password(validated_data['password'])
		user.save()

		# create profile
		print profile_data
		profile = Profile.objects.create(
			user = user,
			**profile_data
		)
		return user

