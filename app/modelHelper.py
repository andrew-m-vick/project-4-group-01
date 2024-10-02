import pickle
import pandas as pd

class ModelHelper:
    def __init__(self):
        self.model_path = "car_model.pkl"  # Update if your path is different
        self.model = self.load_model()

    def load_model(self):
        with open(self.model_path, 'rb') as f:
            model = pickle.load(f)
        return model

    def makePredictions(self, miles, year, vehicle_type, transmission, make, body_type, drivetrain, fuel_type, engine_block, state):
        # Create a DataFrame
        data = {
            'miles': [miles],
            'year': [year],
            'vehicle_type': [vehicle_type],
            'transmission': [transmission],
            'make': [make],
            'body_type': [body_type],
            'drivetrain': [drivetrain],
            'fuel_type': [fuel_type],
            'engine_block': [engine_block],
            'state': [state]
        }
        df = pd.DataFrame(data)

        # Make predictions
        prediction = self.model.predict(df)
        return prediction