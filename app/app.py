from flask import Flask, render_template, request
import pandas as pd
import pickle
from modelHelper import preprocess_input

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("models/car_model.pkl", "rb"))

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":

        # Get the user's input from the form
        miles = request.form["miles"]
        year = request.form["year"]
        make = request.form["make"]
        body_type = request.form["body_type"]
        vehicle_type = request.form["vehicle_type"]
        drivetrain = request.form["drivetrain"]
        transmission = request.form["transmission"]
        fuel_type = request.form["fuel_type"]
        engine_size = request.form["engine_size"]
        engine_block = request.form["engine_block"]
        state = request.form["state"]

        # Create a DataFrame from the user's input
        data = {
            "miles": miles,
            "year": year,
            "make": make,
            "body_type": body_type,
            "vehicle_type": vehicle_type,
            "drivetrain": drivetrain,
            "transmission": transmission,
            "fuel_type": fuel_type,
            "engine_size": engine_size,
            "engine_block": engine_block,
            "state": state
        }

        # Preprocess the data
        data = preprocess_input(data)

        # Make a prediction
        prediction = model.predict(data)[0]

        # Render the results template with the prediction
        return render_template("results.html", prediction=prediction)

    # If the request method is GET, render the prediction form
    return render_template("prediction.html")

@app.route("/tableau")
def map():
    return render_template("tableau.html")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

if __name__ == '__main__':
    app.run(debug=True) 