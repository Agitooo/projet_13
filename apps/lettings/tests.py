from django.test import TestCase
from django.urls import reverse
from apps.lettings.models import Address, Letting


# Test de la page /lettings
class LettingsTest(TestCase):

    def test_lettings_index(self):
        response = self.client.get(reverse("lettings:index"))
        assert response.status_code == 200
        assert b"<title>Lettings</title>" in response.content

    def setUp(self):
        self.address = Address.objects.create(
            number=1, street="street", city="city",
            state="state", zip_code=28170, country_iso_code="FRA"
        )
        self.lettings = Letting.objects.create(title="Letting Test", address=self.address)

    def test_lettings_detail(self):
        response = self.client.get(reverse("lettings:letting", args=[1]))
        assert response.status_code == 200
        assert b"<title>Letting Test</title>" in response.content
