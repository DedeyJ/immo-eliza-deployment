# schema.py
import pandas as pd
from pydantic import BaseModel, Field

class PropertyInput(BaseModel):
    property_type: str = Field(..., description="Type of property")
    subproperty_type: str = Field(..., description="Subtype of property")
    zip_code: str = Field(..., description="Zip code of property")
    total_area_sqm: float = Field(..., description="Total area of the property in square meters")
    surface_land_sqm: float = Field(..., description="Surface land area of the property in square meters")
    nbr_bedrooms: float = Field(..., description="Number of bedrooms in the property")
    terrace_sqm: float = Field(..., description="Size of the terrace in square meters")
    garden_sqm: float = Field(..., description="Size of the garden in square meters")
    primary_energy_consumption_sqm: float = Field(..., description="Primary energy consumption of the property in square meters")
    state_building: str = Field(..., description="State of the building")
    

