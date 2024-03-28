# schema.py
import pandas as pd
from pydantic import BaseModel, Field

df = pd.read_csv(r"./properties.csv")
property_list = df["property_type"].unique().tolist()


class PropertyInput(BaseModel):
    property_type: str = Field(..., description="Type of property")
    subproperty_type: str = Field(..., description="Subtype of property")
    zip_code: str = Field(min_length=4, max_length=4, pattern=r"^[0-9]{4}$", description="Zip code of property")
    total_area_sqm: float = Field(..., ge=18, description="Total area of the property in square meters")
    surface_land_sqm: float = Field(..., ge=18, description="Surface land area of the property in square meters")
    nbr_bedrooms: float = Field(..., ge=1, description="Number of bedrooms in the property")
    terrace_sqm: float = Field(..., ge=0, description="Size of the terrace in square meters")
    garden_sqm: float = Field(..., ge=0, description="Size of the garden in square meters")
    primary_energy_consumption_sqm: float = Field(..., description="Primary energy consumption of the property in square meters")
    state_building: str = Field(..., description="State of the building")

    class Config:
        schema_extra = {
            "example": {
                "property_type": "HOUSE",
                "subproperty_type": "HOUSE",
                "zip_code": "9960",
                "total_area_sqm": 18,
                "surface_land_sqm": 18,
                "nbr_bedrooms": 1,
                "terrace_sqm": 0,
                "garden_sqm": 0,
                "primary_energy_consumption_sqm": 100,
                "state_building": "AS_NEW"
            }
        }
    

