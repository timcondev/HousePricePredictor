
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PredictInputSerializer
from house_app.ml_model import predict_price
from house_app.models import HousePrediction
import io
import pandas as pd

def sanitize_string_fields(data, fields):
    for field in fields:
        data[field] = str(data.get(field, ''))
    return data

@api_view(['POST'])
def predict_api(request):
    serializer = PredictInputSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data

        price = predict_price(data)
        HousePrediction.objects.create(**data, predicted_price=price)
        return Response({'predicted_price': round(price, 2)}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def history_api(request):
    queryset = HousePrediction.objects.all().order_by('-created_at')[:100]
    data = [{
        "city": obj.city,
        "latitude": obj.latitude,
        "longitude": obj.longitude,
        "predicted_price": round(obj.predicted_price, 2)
    } for obj in queryset]
    return Response(data)


@api_view(['POST'])
def upload_csv_api(request):
    csv_file = request.FILES['csv_file']
    decoded_file = csv_file.read().decode('utf-8')
    df = pd.read_csv(io.StringIO(decoded_file))

    required_columns = [
        "city", "latitude", "longitude", "bed", "bath", "sqft",
        "pricePerSf", "lotArea", "zipCode", "lotAreaType", "homeType"
    ]

    if not set(required_columns).issubset(df.columns):
        return Response({'error': 'Missing required columns in CSV.'}, status=status.HTTP_400_BAD_REQUEST)

    df = df.dropna(subset=required_columns)

    predictions = []
    for i, (_, row) in enumerate(df.iterrows()):
        print(f"[UPLOAD] Predicting row {i + 1} of {len(df)}")
        try:
            data = row[required_columns].to_dict()

            # Optional: sanitize string fields for consistency
            data = sanitize_string_fields(data, ["city", "homeType", "lotAreaType", "zipCode"])

            prediction = predict_price(data)

            # Save to DB
            HousePrediction.objects.create(**data, predicted_price=prediction)

            predictions.append({
                "city": data["city"],
                "latitude": data["latitude"],
                "longitude": data["longitude"],
                "predicted_price": round(prediction, 2)
            })

        except Exception as e:
            print(f"[UPLOAD] Error in row {i + 1}: {e}")

    print("[UPLOAD] Finished all predictions.")
    return Response(predictions, status=status.HTTP_200_OK)
