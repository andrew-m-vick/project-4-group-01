$(document).ready(function () {
    console.log("Page Loaded");
  });
  
  function makePredictions(event) {
    console.log("makePredictions() function called");
    event.preventDefault(); // Prevent default form submission
  
    // Get input values from the form (in the new order)
    var make = $("#make").val();
    var body_type = $("#body_type").val();
    var miles = $("#miles").val();
    var year = $("#year").val();
    var vehicle_type = $("#vehicle_type").val();
    var transmission = $("#transmission").val();
    var drivetrain = $("#drivetrain").val();
    var fuel_type = $("#fuel_type").val();
    var engine_size = $("#engine_size").val(); // Get engine_size
    var engine_block = $("#engine_block").val();
    var state = $("#state").val();
  
    // Input validation
    var isValid = true;
  
    if (
      !make ||
      !body_type ||
      !miles ||
      !year ||
      !vehicle_type ||
      !transmission ||
      !drivetrain ||
      !fuel_type ||
      !engine_size ||
      !engine_block ||
      !state
    ) {
      alert("Please fill in all fields.");
      isValid = false;
    }
  
    if (!isValid) {
      return;
    }
  
    // Create the payload
    var payload = {
      make: make,
      body_type: body_type,
      miles: miles,
      year: year,
      vehicle_type: vehicle_type,
      transmission: transmission,
      drivetrain: drivetrain,
      fuel_type: fuel_type,
      engine_size: engine_size, // Include engine_size
      engine_block: engine_block,
      state: state,
    };
  
    // Perform a POST request to the query URL
    $.ajax({
      type: "POST", // Changed to POST
      url: "/makePredictions", // URL remains the same
      contentType: "application/json;charset=UTF-8",
      data: JSON.stringify({ data: payload }),
      success: function (returnedData) {
        console.log(returnedData);
  
  
        // You don't need to parse the prediction here since it's already formatted in app.py
        var prediction = returnedData["prediction"];
        $("#price").text(`${prediction}`);
        $("#prediction-result").show();
        $("#prediction-form").hide();
      },
      error: function (XMLHttpRequest, textStatus, errorThrown) {
        alert("Status: " + textStatus);
        alert("Error: " + errorThrown);
      },
    });
  }