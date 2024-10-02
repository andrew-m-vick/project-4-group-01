import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

class ModelHelper:
    def __init__(self):
        self.model_path = "car_model.pkl"  # Update if your path is different
        self.model = self.load_model()

    def load_model(self):
        with open(self.model_path, 'rb') as f:
            model = pickle.load(f)
        return model

    def label_engine_size(self, engine):
        if 0.1 <= engine < 2:
            return 1
        elif 2 <= engine < 3:
            return 2
        elif 3 <= engine < 4:
            return 3
        elif 4 <= engine < 5:
            return 4
        elif 5 <= engine < 6:
            return 5
        elif 6 <= engine < 7:
            return 6
        elif 7 <= engine < 8:
            return 7
        else:
            return 0

    def makePredictions(self, make, body_type, miles, year, vehicle_type, transmission, drivetrain, fuel_type, engine_size, engine_block, state):
        # 1. Cleaning (assuming engine_size is a direct input)
        engine_size = 0 if engine_size == 'E' else float(engine_size)

        # 2. Binning
        engine_size = self.label_engine_size(engine_size)

        # 3. Scaling
        scaler = StandardScaler()
        engine_size = scaler.fit_transform([[engine_size]])[0][0]  # Scale the value

        # Create a DataFrame
        data = {
            'make': [make],
            'body_type': [body_type], 
            'miles': [miles],
            'year': [year],
            'vehicle_type': [vehicle_type],
            'transmission': [transmission], 
            'drivetrain': [drivetrain],
            'fuel_type': [fuel_type],
            'engine_size': [engine_size], 
            'engine_block': [engine_block],
            'state': [state] 
        }
        df = pd.DataFrame(data)

        # Make predictions
        prediction = self.model.predict(df)
        return prediction