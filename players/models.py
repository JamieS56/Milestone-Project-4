from django.db import models

# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=254)
    number = models.IntegerField(null=False)
    position = models.CharField(max_length=15)
    apearences = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()
    clean_sheets = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    image_url = models.CharField(max_length=100, null=True,
                                                         blank=True)
    def __str__(self):
        return self.name
