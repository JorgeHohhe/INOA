from django.db import models

class AssetConfiguration(models.Model):
    asset_name = models.CharField(max_length=20)
    upper_tunnel = models.DecimalField(max_digits=10, decimal_places=2)
    bottom_tunnel = models.DecimalField(max_digits=10, decimal_places=2)
    checking_frequency = models.PositiveIntegerField()

    def __str__(self):
        return self.asset_name
