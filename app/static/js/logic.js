$(document).ready(function() {
    console.log("Page Loaded");

    $("#filter").click(function() {
        makePredictions();
    });
});

function makePredictions(event) {
    event.preventDefault();
    // Get input values from the form 
    var miles = $("#miles").val();
    var year = $("#year").val();
    var vehicle_type = $("#vehicle_type").val();
    var transmission = $("#transmission").val();
    var make = $("#make").val();
    var body_type = $("#body_type").val();
    var drivetrain = $("#drivetrain").val();
    var fuel_type = $("#fuel_type").val();
    var engine_block = $("#engine_block").val();
    var state = $("#state").val();

    // Input validation (add more specific checks as needed)
    if (!miles || !year || !vehicle_type || !transmission || !make || !body_type || !drivetrain || !fuel_type || !engine_block || !state) {
        alert("Please fill in all fields.");
        return;
    }

    // Create the payload
    var payload = {
        "miles": miles,
        "year": year,
        "vehicle_type": vehicle_type,
        "transmission": transmission,
        "make": make,
        "body_type": body_type,
        "drivetrain": drivetrain,
        "fuel_type": fuel_type,
        "engine_block": engine_block,
        "state": state
    };

    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",  // Changed to POST
        url: "/makePredictions",  // URL remains the same
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            console.log(returnedData);

            // You don't need to parse the prediction here since it's already formatted in app.py
            var prediction = returnedData["prediction"]; 
            $("#price").text(`Predicted Car Price: ${prediction}`);
            $("#prediction-result").show();
            $("#prediction-form").hide();
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });
}