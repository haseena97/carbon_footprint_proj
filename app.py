from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle


app = Flask(__name__)
model = pickle.load(open("model_file.p", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        
        # age
        passenger_age = request.form["Passenger_Car_Age"]
        light_truck_age = request.form["Light_Truck_Age"]
        light_vehicle_age = request.form["Light_vehicle_Age"]
        age = passenger_age + light_truck_age + light_vehicle_age

        # eff
        domestic_eff = request.form["Domestic_EFF"]
        light_truck_eff = request.form["Light_Truck_EFF"]
        short_wheel_eff = request.form["LDV_SWB_EFF"]
        eff = domestic_eff + light_truck_eff + short_wheel_eff
        
        # ratio
        ratio_eff_age = age/eff
        
        
        
        prediction=model.predict([[
           'Combination_Truck_road_BTU', 'Railways_BTU', 'Water_BTU',
       'Domestic_EFF', 'Light_Truck_EFF', 'LDV_SWB_EFF', 'Passenger_Car_Age',
       'Light_Truck_Age', 'Light_vehicle_Age',
       'Demand_petroleum_transportation)mil_lit',
       'Average_MC/15000_miles(dollars)', ratio_eff_age
        ]])

        output=round(prediction[0],2)

        return render_template('index.html',prediction_text="Your Carbon Emission is {} million/tonnes".format(output))


    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)

