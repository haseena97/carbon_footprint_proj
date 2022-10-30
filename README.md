# Analysis of Carbon Footprint in the Logistics Industry
- Created a web app that allow client to predict their annual carbon footprint based on their vehicles' fuel consumption and other variables.
- Use permutation importance to identify major contributors to carbon emission.
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
<p float="left">
  <img src="https://user-images.githubusercontent.com/71859510/198867808-702dc964-35ee-4433-9f4c-1f4cd5e418b5.png" width="400" height="250">
  <img src="https://user-images.githubusercontent.com/71859510/198867974-b437fdc2-4599-4ec8-abd1-3b14a3d9d6c3.png" width="400" height="250">
  <img src="https://user-images.githubusercontent.com/71859510/198867877-a42e0204-4077-4e47-aa1d-0e2d539b90c0.png" width="498" height="338">
</p>

## Model Building
First, I performed feature selection to address multicollinearity. I also split the data into train and tests sets with a test size of 20%.

I tried different linear and tree-based models that I think would be a good fit for small dataset with outliers and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret.<br>
Models:
- Linear Regression
- Lasso Regression
- Random Forest Regressor
- Huber Regressor
- Theil-sen Regressor
- RANSAC Regressor
- XGBoost
- Gradient-Boosting Regressor<br>

I used `permutation importance` on Huber Regressor to identify major contributors to carbon emission:
![image](https://user-images.githubusercontent.com/71859510/198869546-456a0173-00bd-45d8-bd29-855b4ac51894.png)

I used permutation importance because it is model agnostic.
## Model Performance
![image](https://user-images.githubusercontent.com/71859510/198868514-15084160-80be-48c7-ae62-3546a0ac8067.png)<br>
The **Huber Regressor model** far outperformed the other approaches on the test and validation sets. Other models heavily overfit the data.
## Productionization
In this step, I built a flask API endpoint that was hosted on [Heroku](https://carbon-footprint-prediction.herokuapp.com/) by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values input by client and returns an estimated carbon emission.





