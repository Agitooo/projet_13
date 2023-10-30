from django.test import TestCase
from django.urls import reverse
from apps.profiles.models import Profile
from django.contrib.auth.models import User


# Test de la page /profile
class ProfilesTest(TestCase):

    def test_profiles_index(self):
        response = self.client.get(reverse("profiles:index"))
        assert response.status_code == 200
        assert b"<title>Profiles</title>" in response.content

    def setUp(self):
        self.user = User.objects.create(
            username="UsernameTest", password="PasswordTest", email="test@test.test"
        )
        self.profiles = Profile.objects.create(user=self.user, favorite_city="test fav city")

    def test_profiles_detail(self):
        response = self.client.get(reverse('profiles:profile', args=["UsernameTest"]))
        assert response.status_code == 200
        assert b"<title>UsernameTest</title>" in response.content
