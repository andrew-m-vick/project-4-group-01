import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

def preprocess_input(input_data):
    # Convert the input data to a DataFrame
    data = pd.DataFrame({
        "miles": [input_data["miles"]],
        "year": [input_data["year"]],
        "make": [input_data["make"]],
        "body_type": [input_data["body_type"]],
        "vehicle_type": [input_data["vehicle_type"]],
        "drivetrain": [input_data["drivetrain"]],
        "transmission": [input_data["transmission"]],
        "fuel_type": [input_data["fuel_type"]],
        "engine_size": [input_data["engine_size"]],
        "engine_block": [input_data["engine_block"]],
        "state": [input_data["state"]]
    })

    # Preprocess the data
    # Define preprocessing for numeric features
    numeric_features = ['miles', 'year', 'engine_size']
    numeric_transformer = Pipeline(steps=[
        ('scaler', StandardScaler())])

    # Define preprocessing for the binary features
    binary_features = ['vehicle_type', 'transmission']
    binary_transformer = Pipeline(steps=[
        ('label', OrdinalEncoder())])

    # Define preprocessing for categorical features
    categorical_features = ['make', 'body_type', 'drivetrain', 'fuel_type', 'engine_block', 'state']
    categorical_transformer = Pipeline(steps=[
        ('onehot', OneHotEncoder(handle_unknown='ignore'))])

    # Combine preprocessing for numeric and categorical features
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('binary', binary_transformer, binary_features),
            ('cat', categorical_transformer, categorical_features)])

    # Transform the data
    data = preprocessor.fit_transform(data)

    return data