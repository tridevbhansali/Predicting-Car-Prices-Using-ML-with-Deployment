from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from joblib import load
import numpy as np

models = load(".\static\model_name.joblib")
ml_model= load(".\static\carwala_model.joblib")
le_company = load(".\static\le_company.joblib")
le_model = load(".\static\le_model.joblib")
le_fuel = load(".\static\le_fuel.joblib")
brands = load(".\static\Brand_name.joblib")
years = load(".\static\year.joblib")


def car_predict(year,comp,mod,fuel,km):
    global ml_model
    global le_company 
    global le_model 
    global le_fuel 
    comp = np.squeeze(le_company.transform([comp]))
    mod = np.squeeze(le_model.transform([mod]))
    fuel = np.squeeze(le_fuel.transform([fuel]))
    predicted = ml_model.predict([[year,comp,mod,fuel,km]])
    return predicted

def model_name():
    global models
    model = []
    for i in models:
        model.append(i)
    return model

def brand_name():
    global brands
    brand = []
    for i in brands:
        brand.append(i)
    return brand
    
def year():
    global years
    year = []
    for i in years:
        year.append(int(i))
    return year
