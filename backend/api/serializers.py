from rest_framework import serializers

class PredictInputSerializer(serializers.Serializer):
    bed = serializers.FloatField()
    bath = serializers.FloatField()
    sqft = serializers.FloatField()
    pricePerSf = serializers.FloatField()
    lotArea = serializers.FloatField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    zipCode = serializers.CharField()
    city = serializers.CharField()
    lotAreaType = serializers.CharField()
    homeType = serializers.CharField()
