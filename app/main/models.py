from django.db import models

# Create your models here.
class Data(models.Model):
    Country = models.CharField(max_length = 50)
    Year = models.IntegerField()
    Rank = models.CharField(max_length = 50)
    Total = models.FloatField()
    S1 = models.FloatField()
    S2 = models.FloatField()
    C3 = models.FloatField()
    E3 = models.FloatField()
    E2 = models.FloatField()
    E1 = models.FloatField()
    P1 = models.FloatField()
    P2 = models.FloatField()
    P3 = models.FloatField()
    C1 = models.FloatField()
    C2 = models.FloatField()
    X1 = models.FloatField()

    def __str__(self):
        return self.Country
    
    class Meta():
        verbose_name = 'Data'
        verbose_name_plural = 'Data'