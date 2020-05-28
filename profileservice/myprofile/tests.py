import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from myprofile.models import Profile


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {
                'username': 'user1234',
                'email': 'user1234@email.com',
                'password': '1234qwer',
                'profile': {
                        'job': ' Programmer',
                        'city': 'Curitiba'
                        }
                }
        response = self.client.post('/api/users/', json.dumps(data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ProfileViewSetTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='user1234@email.com',
                                             password='1234qwer')

        self.profile = Profile.objects.create(
                user=self.user, city='Somewhere', job='Some job')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_profile_list_authenticated(self):

        response = self.client.get(reverse('api:profile-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(reverse('api:profile-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_detail_retrieve(self):
        response = self.client.get(reverse('api:profile-detail',
                                           kwargs={'pk': self.profile.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['job'], 'Some job')
        self.assertEqual(response.data['city'], 'Somewhere')

    def test_profile_update_by_owner(self):
        response = self.client.put(reverse('api:profile-detail',
                                           kwargs={'pk': self.profile.pk}),
                                   {'city': 'Nowhere',
                                    'job': 'Guido\'s assistant'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),
                         {'id': self.profile.id,
                          'city': 'Nowhere',
                          'job': 'Guido\'s assistant',
                          'heart_count': 0,
                          'messages_count': 0,
                          'rate_average': None})

    def test_profile_update_by_random_user(self):
        random_user = User.objects.create_user(username='other_user',
                                               password='1234qwer')
        self.client.force_authenticate(user=random_user)
        response = self.client.put(reverse('api:profile-detail',
                                           kwargs={'pk': self.profile.pk}),
                                   {'job': 'PHP programmer'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_profile_update_by_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.put(reverse('api:profile-detail',
                                           kwargs={'pk': self.profile.pk}),
                                   {'job': 'PHP programmer'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
