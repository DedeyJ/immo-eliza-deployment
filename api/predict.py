import pickle

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LinearRegression, LassoCV
from sklearn.model_selection import train_test_split
from sklearn.impute import KNNImputer
from sklearn.compose import ColumnTransformer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import KNNImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import json

def make_prediction(df):
    # Load the saved model
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    
    return model.predict(df)


# with open('house.json') as f:
#     json_file = json.load(f)



# df = pd.json_normalize(json_file)
# y_pred = make_prediction(df)
# print(y_pred)