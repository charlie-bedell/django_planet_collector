from django.db import models

# Create your models here.

planet_types = [
    ('N/A', 'Unknown'),
    ('TP', 'Terrestial Planet'),
    ('GG', 'Gas Giant'),
    ('IG', 'Ice Giant'),
    ('DP', 'Dwarf Planet'),
]

ring_choices = [
    ('Y', 'Yes'),
    ('N', 'No'),
    ('N/A', 'Unknown'),
]


class Planet(models.Model):
    name = models.CharField(max_length=100)
    planet_type = models.CharField(max_length=3, choices=planet_types)
    mass = models.DecimalField(max_digits=10, decimal_places=5)
    equitorial_diameter = models.DecimalField(max_digits=6, decimal_places=4)
    semi_major_axis = models.DecimalField(max_digits=5, decimal_places=2)
    orbital_period = models.DecimalField(max_digits=7, decimal_places=2)
    inclination_to_the_ecliptic = models.DecimalField(max_digits=5, decimal_places=3)
    orbital_eccentricity = models.DecimalField(max_digits=4, decimal_places=3)
    rotation_period = models.DecimalField(max_digits=5, decimal_places=2)
    confirmed_moons = models.PositiveSmallIntegerField()
    axial_tilt = models.DecimalField(max_digits=5, decimal_places=2)
    rings = models.CharField(max_length=3, choices=ring_choices)
    atmosphere = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} - {self.planet_type}"
