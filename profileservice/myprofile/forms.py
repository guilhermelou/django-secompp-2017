from django.forms import ModelForm
from myprofile.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['job', 'city']
