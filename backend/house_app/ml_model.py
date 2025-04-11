
import numpy as np
import pandas as pd
import joblib
from functools import lru_cache

@lru_cache(maxsize=1)
def get_pipeline():
    preprocessor = joblib.load("model/preprocessor.pkl")
    model = joblib.load("model/model_linear.pkl")
    return preprocessor, model

def predict_price(raw_input_dict):
    """
    raw_input_dict: dictionary of raw form inputs with keys:
    'bed', 'bath', 'sqft', 'pricePerSf', 'lotArea', 'latitude', 'longitude',
    'zipCode', 'city', 'lotAreaType', 'homeType'
    """
    preprocessor, model = get_pipeline()

    # Build input DataFrame
    input_df = pd.DataFrame([{
        'bed': float(raw_input_dict['bed']),
        'bath': float(raw_input_dict['bath']),
        'sqft': float(raw_input_dict['sqft']),
        'pricePerSf': float(raw_input_dict['pricePerSf']),
        'lotArea': float(raw_input_dict['lotArea']),
        'latitude': float(raw_input_dict['latitude']),
        'longitude': float(raw_input_dict['longitude']),
        'zipCode': str(raw_input_dict['zipCode']),
        'city': str(raw_input_dict['city']),
        'lotAreaType': str(raw_input_dict['lotAreaType']),
        'homeType': str(raw_input_dict['homeType']),
    }])

    # Transform and predict
    X = preprocessor.transform(input_df)
    prediction = model.predict(X)

    # Return the first predicted value, rounded
    return float(np.round(prediction[0], 2))
