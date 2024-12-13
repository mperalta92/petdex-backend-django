from django.db import models

class Dog(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    temperament = models.CharField(max_length=255)
    weight = models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    life_span = models.CharField(max_length=50)
    bred_for = models.CharField(max_length=255)
    image = models.URLField(max_length=200)

    def __str__(self):
        return self.name
    
class Cat(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    weight = models.CharField(max_length=50)
    temperament = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    life_span = models.CharField(max_length=50)
    adaptability = models.IntegerField()
    affection_level = models.IntegerField()
    energy_level = models.IntegerField()
    health_issues = models.IntegerField()
    intelligence = models.IntegerField()
    stranger_friendly = models.IntegerField()
    child_friendly = models.IntegerField()
    hairless = models.BooleanField()
    natural = models.BooleanField()
    short_legs = models.BooleanField()
    rare = models.BooleanField()
    indoor = models.BooleanField()
    image = models.URLField(max_length=200)
    wikipedia_url = models.URLField(max_length=200)

    def __str__(self):
        return self.name