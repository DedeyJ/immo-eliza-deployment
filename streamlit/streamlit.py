import streamlit as st
import requests
import pandas as pd
# Streamlit UI elements to take user input
# st.title("Price Prediction App")
df = pd.read_csv("properties.csv")

# postcode = pd.read_excel("zipcodes_num_nl_new.xls")

# def round_down_to_100(value):
#     if value < 0:
#       return (value // 100) * 100 -100
#     else:
#        return (value // 100) * 100



# property_types = df["property_type"].unique()
# property_subtypes = {}

# for property in property_types:
#    property_subtypes[property] = df.loc[df["property_type"]==property, "subproperty_type"].unique().tolist()


# def format_input_for_display(input_string):
#     formatted_string = input_string.replace("_", " ").lower().capitalize()
#     return formatted_string
st.title("Immoweb Price Prediction")
data = {}

data["property_type"] = st.selectbox('Choose Property Type', list(property_subtypes.keys()))
subproperty_type_options = property_subtypes.get(data["property_type"], [])
data["subproperty_type"] = st.selectbox('Select Subproperty Type', subproperty_type_options)
data["zip_code"] = str(st.selectbox('Zip code',options=(v for v in df["zip_code"].unique())))
data["total_area_sqm"] = st.number_input('Total Area (sqm)', min_value=18.0)
data["surface_land_sqm"] = st.number_input('Surface Land Area (sqm)', min_value=18.0)
data["nbr_bedrooms"] = st.number_input('Number of Bedrooms', min_value=1, step=1)
data["terrace_sqm"] = st.slider('Terrace Size (sqm)', min_value=0.0, max_value= 1000.0)
data["garden_sqm"] = st.slider('Garden Size (sqm)', min_value=0.0, max_value= 1000.0)
data["primary_energy_consumption_sqm"] = st.slider('Primary Energy Consumption (sqm)', min_value=-100, max_value= 1500)
data["state_building"] = st.selectbox('State of the Building', options=(v for v in df["state_building"].unique() if v != "MISSING"))



# Button to trigger prediction
if st.button("Predict"):
    # Prepare user input as a dictionary
    # Send data to FastAPI backend for prediction
    response = requests.post("https://immo-eliza-deployment-v9xy.onrender.com/predict", json=data)
    prediction = response.json()["prediction"]
    st.write(f"Prediction: €{round(prediction,2)}")