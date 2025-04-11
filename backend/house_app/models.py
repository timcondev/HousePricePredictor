from django.db import models

class HousePrediction(models.Model):
    bed = models.FloatField()
    bath = models.FloatField()
    sqft = models.FloatField()
    pricePerSf = models.FloatField()
    lotArea = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    zipCode = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    lotAreaType = models.CharField(max_length=20)
    homeType = models.CharField(max_length=30)

    predicted_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
