![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://<your-custom-subdomain>.streamlit.app)

# immo-eliza-deployment



In the previous parts of the project, we scraped data from a reputable immo website from Belgium, we analysed the data, and built a model for making price predictions. 

In this part of the preoject we modeled an api and a streamlit web app, which are both deployed on Render.

## Overview

### API
The API makes a prediction of house/apartment prices based on certain features.
Example json:
~~~
{
  "property_type": "HOUSE",
  "subproperty_type": "HOUSE",
  "zip_code": "9060",
  "total_area_sqm": 10,
  "surface_land_sqm": 10,
  "nbr_bedrooms": 2,
  "terrace_sqm": 10,
  "garden_sqm": 2,
  "primary_energy_consumption_sqm": 23,
  "state_building": "AS_NEW"
}
~~~

### Streamlit app 
The Streamlit app provides an easy user interface to provide the necessary input which are sent to the API for making the prediction.

## Folder Structure

The project is divided in two folders, allowing two services to be deployed in Render.

├─ api/
└─ streamlit/

## Installation

To run locally clone the github repository to your local folder. The requirements for both the API and streamlit app can be found in the requirements.txt in their respective folders.

To run the project locally, first run following command from Terminal in API folder:
~~~
uvicorn app:app --host 0.0.0.0 --port 8000 
~~~

To run streamlit, you'll have to make some changes in the streamlit.py file in the streamlit folder:
![Streamlit Code](images\streamlit.png)
Change the site to "http://0.0.0.0:8000/predict" and save the file.
Now run following command in Terminal from streamlit folder:
~~~
streamlit run streamlit.py
~~~
It will provide you an adress to see the streamlit web app.


## Usage

Explain how to use both the API and the Streamlit app. Provide examples or screenshots if applicable.
API

    Instructions for accessing and interacting with the API.
    Endpoints and their functionalities.

Streamlit App

    How to run the Streamlit app locally.
    Features and functionalities of the app.

## Deployment

The required Dockerfiles are already provided in the project. 
Simply push to your own github repository, and create the required webservices for both the  api and the streamlit app.

Create webservice:
![Create Webserice](images\create_webservice.jpg)
Build and deploy from git Repository:
![Build from repo](images\build_from_repo.jpg)
If your github account is linked with render, you should be able to find them, otherwise you can connect to public repo using your repo link.
Configuration:
![Configuration](images\Configuration.jpeg)
Give it a name, specify the region, and specify the root directory as the folder which you want to deploy. So for fastapi you fill in "api". The runtime is Docker.
Make sure to choose free, and click "Creat Webservice".

Creating the Streamlit app webservice follows the same path, but make sure to change the response request in the streamlit.py file first to the api webservice you just created.

## Example
### API
https://immo-eliza-deployment-v9xy.onrender.com/docs#/

### Streamlit app
https://immo-eliza-deployment-1-n68p.onrender.com/

## Limitations
For the moment it requires you to manually change the post request in the code for the streamlit app. Want to change it so it can be asked as a variable in Render.

## Timeline
This project was completed in 5 days.

## Contact

Jens Dedeyne: [Linkedin](https://www.linkedin.com/in/jens-dedeyne/)