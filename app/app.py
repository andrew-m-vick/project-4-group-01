from flask import Flask, render_template, request, jsonify
from modelHelper import ModelHelper

# Create an instance of Flask
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

modelHelper = ModelHelper()

# Route to render home.html
@app.route("/")
def home():
    # Return template and data
    return render_template("home.html")

@app.route("/about_us")
def about_us():
    # Return template and data
    return render_template("about_us.html")

@app.route("/tableau")
def tableau():
    # Return template and data
    return render_template("tableau.html")


@app.route("/resources")
def resources():
    # Return template and data
    return render_template("resources.html")

@app.route("/predict")  # Changed route to /predict
def predict():
    return render_template("index.html")  # Render index.html for the /predict route

@app.route("/makePredictions", methods=["POST"])
def make_predictions():
    content = request.json["data"]
    print(content)

    # parse
    miles = float(content["miles"])
    year = float(content["year"])
    vehicle_type = content["vehicle_type"]
    transmission = content["transmission"]
    make = content["make"]
    body_type = content["body_type"]
    drivetrain = content["drivetrain"]
    fuel_type = content["fuel_type"]
    engine_block = content["engine_block"]
    state = content["state"]

    preds = modelHelper.makePredictions(miles, year, vehicle_type, transmission, make, body_type, drivetrain, fuel_type, engine_block, state)

    # You may want to format the prediction before sending it back
    formatted_prediction = f"${preds[0]:.2f}"  # Example: format as a dollar amount

    return jsonify({"ok": True, "prediction": formatted_prediction})

#############################################################

@app.after_request
def add_header(r):
    # Add headers to both force latest IE rendering engine or Chrome Frame,
    # and also to cache the rendered page for 10 minutes.
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#main
if __name__ == "__main__":
    app.run(debug=True)