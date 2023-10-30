from django.test import TestCase
from django.urls import reverse


# Test de la page / (home)
class HomeIndexTest(TestCase):

    def test_home_index(self):

        response = self.client.get(reverse("home:index"))
        assert response.status_code == 200
        assert b"<title>Holiday Homes</title>" in response.content
