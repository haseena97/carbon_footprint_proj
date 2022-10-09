from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle
from sklearn.cluster import KMeans

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
        
        features = [Demand_petroleum,cost,ratio_eff_age]

        # Standardize
        X_scaled = features
        X_scaled = (X_scaled - X_scaled.mean(axis=0)) / X_scaled.std(axis=0)

        kmeans = KMeans(n_clusters=10, n_init=10, random_state=0)
        Cluster_Age = kmeans.fit_predict(X_scaled)
        
        # load model
        model = load_models()
        prediction=model.predict([[
           Combination_Truck_road_BTU, Railways_BTU, Water_BTU,
       domestic_eff, passenger_eff,  short_wheel_eff, passenger_age,
       light_truck_age, light_vehicle_age,
       Demand_petroleum, cost, ratio_eff_age,Cluster_Age
        ]])

        output=round(prediction[0],2)
        
            
        return render_template('index.html',prediction_text="Your Carbon Emission is {} million/tonnes".format(output))
                              


    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)



