from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model
loaded_model=pickle.load(open("finalized_model_Log.sav",'rb'))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    Number_of_Trips = float(request.form["Number_of_Trips"])
    Operating_Hours = float(request.form["Operating_Hours "])
    Days_Since_Maintenance= float(request.form["Days_Since_Maintenance"])

    #data = np.array([[Number_of_Trips,Operating_Hours ,Days_Since_Maintenance]])
    
    data = pd.DataFrame(
    np.array([[[Number_of_Trips,Operating_Hours ,Days_Since_Maintenance]]),
    columns=["Number_of_Trips", "Operating_Hours", "Days_Since_Maintenance"]
)


    prediction = model.predict(scaled_data)[0]

    if prediction == 1:
        result = "Maintenance required"
    else:
        result = "Maitenance not required"

    return render_template("result.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)