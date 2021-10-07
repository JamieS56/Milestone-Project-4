from django.db import models

# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=254)
    position = models.CharField(max_length=15)
    apearences = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()
    clean_sheets = models.IntegerField()
    description = models.TextField()
    main_image_url = models.URLField(max_length=1024, null=True, blank=True)
    close_up_image_url = models.URLField(max_length=1024, null=True, 
                                                         blank=True)

    def __str__(self):
        return self.name
