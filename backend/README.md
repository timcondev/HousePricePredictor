# 🧠 Backend – House Price Predictor API

This is the backend server built with Django and Django REST Framework. It exposes REST endpoints for predicting house prices based on a trained TensorFlow model.

## 🚀 Features

- REST API endpoints:
  - `POST /api/predict/` – Predict price for one house
  - `POST /api/upload/` – upload a csv price file
  - `GET /api/history/` – Retrieve recent prediction history
- Preprocessing pipeline saved and reused for inference
- Admin panel via `/admin/`

## 🛠 Setup

```bash
cd backend
py -3.10 -m venv venv 
.\venv\Scripts\activate

pip install -r requirements.txt
```

## ⚙️ Run the Server

```bash
python manage.py makemigrations
python manage.py migrate
python scripts/train_model.py  # If model isn't trained yet
python manage.py runserver
```

Visit API: [http://localhost:8000/api/predict/]

## 🧪 Sample API Call

```json
POST /api/predict/
{
  "bed": 3, "bath": 2, "sqft": 1800, "pricePerSf": 400,
  "lotArea": 5000, "latitude": 43.6, "longitude": -79.5,
  "zipCode": "L6H", "city": "Oakville", 
  "lotAreaType": "sqft", "homeType": "Detached"
}
```
