# Analysis of Carbon Footprint in the Logistics Industry
- Created a web app that allow client to predict their annual carbon footprint based on their vehicles' fuel consumption and other variables.
- Plot permutation importance plot to identify major contributors to carbon emission.
- Optimized linear and tree-based models using GridsearchCV to reach the best model with least MAE score.
- Built a client facing API using flask and host on Heroku.
- Provide solutions for each contributors to carbon emission.

## Codes and Resources Used
**Python Version:** Python 3.9<br>
**Packages:** numpy, matplotlib, seaborn, sklearn, xgboost, flask, json, pickle<br>
**Flask Productionization Github:** https://github.com/PlayingNumbers/ds_salary_proj/tree/master/FlaskAPI<br>
**Flask Productionization Article:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku

## Data
Overall, with each year, we got the following:

- Year
- Vehicles' Age
- Vehicles' Efficiency
- Vehicles' Fuel Consumption
- Petroluem Demand
- Average Maintenance Cost

## Data Cleaning 
Some of the features have more than 40% missing values, so I needed to impute them so that it was usable for our model. I also made the following changes and created the following variables:
- Impute missing values using `front-fill`, `backward-fill`, `Multiple Imputation by Chained Equations (MICE)` and `spline interpolation`.
- Made columns for vehicles' average age and average efficiency
- Made column for vehicles' age to efficiency ratio
- Added a column for vehicles' average maintenance cost to petroluem demand ratio
## EDA
I looked at the distributions of the data which are all numerical variables. Below are a few highlights:
![image](https://user-images.githubusercontent.com/71859510/198867808-702dc964-35ee-4433-9f4c-1f4cd5e418b5.png)








