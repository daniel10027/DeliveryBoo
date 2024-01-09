from django.db import models
from django_countries.fields import CountryField
from django.db import models
from django.urls import reverse
import secrets
import string

progress_values = {
    'En recuperation': 20,
    'Au depot': 40,
    'Au Chargement': 60,
    "En cours d'expedition": 80,
    "En cours de livraison": 90,
    "Colis livré": 100,
}


status = (
    ('En recuperation', 'En recuperation',),
    ('Au depot', 'Au depot',),
    ('Au Chargement', 'Au Chargement',),
    ("En cours d'expedition", "En cours d'expedition",),
    ("En cours de livraison", "En cours de livraison",),
    ("Colis livré", "Colis livré",),
)

class Colis(models.Model):
    """Model definition for Colis."""
    titre = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    source = models.CharField(max_length=150)
    destination = models.CharField(max_length=150)
    proprietaire = models.CharField(max_length=150)
    contact = models.CharField(max_length=20)
    etat = models.CharField(max_length=100, choices=status,)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    code  = models.CharField(max_length=10,editable=False)
    progression = models.IntegerField(default=0)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Colis."""

        verbose_name = 'Colis'
        verbose_name_plural = 'Coliss'

    def dbs(self):
        return f"<ul>" \
               f"<li>Titre: {self.titre}</li>" \
               f"<li>Description: {self.description}</li>" \
               f"<li>Source: {self.source}</li>" \
               f"<li>Destination: {self.destination}</li>" \
               f"<li>Propriétaire: {self.proprietaire}</li>" \
               f"<li>Contact: {self.contact}</li>" \
               f"<li>État: {self.etat}</li>" \
              

    def save(self, *args, **kwargs):
        # Check if the code is already set, i.e., it's an existing object being updated
        self.progression = progress_values.get(self.etat, 0)
        if not self.code:
            # Generate a random 10-character alphanumeric code
            chars = (string.ascii_uppercase + string.digits).upper()
            self.code = ''.join(secrets.choice(chars) for _ in range(10))

            # Ensure the code is unique in the database
            while Colis.objects.filter(code=self.code).exists():
                self.code = ''.join(secrets.choice(chars) for _ in range(10))

        super(Colis, self).save(*args, **kwargs)
        

    def get_absolute_url(self):
        """Return absolute url for Colis."""
        return ('')

    # TODO: Define custom methods here
