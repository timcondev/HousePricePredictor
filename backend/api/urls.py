from django.urls import path
from .views import predict_api, history_api, upload_csv_api
urlpatterns = [
    path('upload/', upload_csv_api),
    path('predict/', predict_api),
    path('history/', history_api),
]