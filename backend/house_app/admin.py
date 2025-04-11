from django.contrib import admin
from .models import HousePrediction

@admin.register(HousePrediction)
class HousePredictionAdmin(admin.ModelAdmin):
    list_display = (
        'bed', 'bath', 'sqft', 'pricePerSf', 'lotArea',
        'latitude', 'longitude', 'zipCode', 'city',
        'lotAreaType', 'homeType', 'predicted_price', 'created_at'
    )
