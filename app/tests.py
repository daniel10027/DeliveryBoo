from django.test import TestCase
from django.urls import reverse
from .models import Colis


class ColisTestCase(TestCase):
    def setUp(self):
        # Set up data for the tests
        self.colis = Colis.objects.create(
            titre="Test Colis",
            description="Description",
            source="Source",
            destination="Destination",
            proprietaire="Owner",
            contact="123456",
            etat="En recuperation",
            active=True,
            progression=20  # You might need to adjust this value based on your requirements
        )

    def test_colis_list_view(self):
        # Test the colis_list view
        response = self.client.get(reverse('colis_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Colis')

    def test_colis_create_view(self):
        # Test the ColisCreateView
        response = self.client.post(reverse('colis_create'), data={
            'titre': 'New Test Colis',
            'description': 'New Description',
            'source': 'New Source',
            'destination': 'New Destination',
            'proprietaire': 'New Owner',
            'contact': '789012',
            'etat': 'Au depot',
            'active': True,
        })
        self.assertEqual(response.status_code, 302)  # 302 is the HTTP status code for a successful redirect

        # Check if the new colis is created
        new_colis = Colis.objects.get(titre='New Test Colis')
        self.assertIsNotNone(new_colis)

    def test_colis_update_view(self):
        # Test the ColisUpdateView
        response = self.client.post(reverse('colis_update', args=[self.colis.id]), data={
            'titre': 'Updated Test Colis',
            'description': 'Updated Description',
            'source': 'Updated Source',
            'destination': 'Updated Destination',
            'proprietaire': 'Updated Owner',
            'contact': '987654',
            'etat': 'Au Chargement',
            'active': False,
        })
        self.assertEqual(response.status_code, 302)  # 302 is the HTTP status code for a successful redirect

        # Check if the colis is updated
        updated_colis = Colis.objects.get(id=self.colis.id)
        self.assertEqual(updated_colis.titre, 'Updated Test Colis')
        self.assertEqual(updated_colis.etat, 'Au Chargement')
        self.assertFalse(updated_colis.active)
