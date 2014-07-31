from django.db import models

# Create your models here.

class Ingredient(models.Model):

    def __unicode__(self):
        return u"%s: %s" % (self.cas, self.name)

    cas = models.CharField(
        max_length=15,
        unique=True)
    name = models.CharField(max_length=30, blank=True)