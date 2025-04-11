# 🎨 Frontend – House Price Predictor UI

This is the React + Tailwind CSS frontend that interacts with the Django REST API to predict house prices.

## 🧭 Features

- Form for predicting single house price
- CSV upload interface for batch predictions
- Prediction history + Google Maps integration
- Responsive UI using Tailwind CSS

## ⚙️ Setup & Run

```bash
cd frontend
npm install
npm run dev
```

Visit UI: [http://localhost:5173]

## 🔌 Backend Proxy

This project uses Vite proxy to forward `/api/` calls to Django running on `localhost:8000`.

Ensure backend is running before testing.
