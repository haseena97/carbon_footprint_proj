from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle


app = Flask(__name__)

def load_models():
    file_name = "models/model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model

@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        
        # age
        passenger_age = float(request.form["Passenger_Car_Age"])
        light_truck_age = float(request.form["Light_Truck_Age"])
        light_vehicle_age = float(request.form["Light_vehicle_Age"])
        age = passenger_age + light_truck_age + light_vehicle_age

        # eff
        domestic_eff = float(request.form["Domestic_EFF"])
        passenger_eff = float(request.form["Passenger_Car_EFF"])
        short_wheel_eff = float(request.form["LDV_SWB_EFF"])
        eff = domestic_eff + passenger_eff + short_wheel_eff
        
        # ratio
        ratio_eff_age = age/eff
        
        Combination_Truck_road_BTU = float(request.form["Combination_Truck_road_BTU"])
        Railways_BTU = float(request.form["Railways_BTU"])
        Water_BTU = float(request.form["Water_BTU"])
        Demand_petroleum = float(request.form["Demand_petroleum_transportation)mil_lit"])
        cost = float(request.form["Average_MC/15000_miles(dollars)"])
        
        
        
        # load model
        model = load_models()
        prediction=model.predict([[
           Combination_Truck_road_BTU, Railways_BTU, Water_BTU,
       domestic_eff, passenger_eff,  short_wheel_eff, passenger_age,
       light_truck_age, light_vehicle_age,
       Demand_petroleum, cost, ratio_eff_age
        ]])

        output=round(prediction[0],2)
        if output < 1000:
            st = 'A'
        elif output < 1400 and output > 1000:
            st = 'B'
        elif output < 1800 and output > 1400:
            st = 'C'
        elif output < 2000 and output > 1800:
            st = 'D'
        else:
            st = 'E'
            
        return render_template('index.html',prediction_text="Your Carbon Emission is {} million/tonnes".format(output),
                               range_text='Your Carbon Footprint Score is {}'.format(st))
                              


    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)



