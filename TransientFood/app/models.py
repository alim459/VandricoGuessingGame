from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=60)
    genre = models.CharField(max_length=60)
    # location = models.Location # ask if this is right??
    opening = models.IntegerField
    closing = models.IntegerField
    # bogusField = models.IntegerField



    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name


    # !!!think about photos/pictures

