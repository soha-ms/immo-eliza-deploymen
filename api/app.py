from fastapi import FastAPI, HTTPException
import os
from pydantic import BaseModel, ValidationError
from api.predict import PreprocesseData
from typing import Optional
from enum import Enum

# Set port to the env variable PORT to make it easy to choose the port on the server
# If the Port env variable is not set, use port 8000
PORT = os.environ.get("PORT", 8000)
app = FastAPI(port=PORT)

class PropertyType(str, Enum):
    house = "HOUSE"
    apartment = "APARTMENT"

class BuildingState(str, Enum):
    to_restore = "TO_RESTORE"
    to_be_done_up = "TO_BE_DONE_UP"
    to_renovate = "TO_RENOVATE"
    just_renovated = "JUST_RENOVATED"
    good = "GOOD"
    as_new = "AS_NEW"


class HeatingType(str, Enum):
    carbon = "CARBON"
    wood = "WOOD"
    pellet = "PELLET"
    fueloil = "FUELOIL"
    gas = "GAS"
    electric = "ELECTRIC"
    solar = "SOLAR"

class Province(str, Enum):    
    brussels = "Brussels"
    antwerp = "Antwerp"
    eastFlanders = "EastFlanders"
    flemish = "Flemish Brabant"
    hainaut = "Hainaut"
    limburg = "Limburg"
    liege = "Liège"
    luxembourg = "Luxembourg"
    namur = "Namur"
    walloon = "Walloon Brabant"
    westFlander = "West Flanders"

class EPC (str, Enum):
    G = 'G'
    F = 'F'
    E = 'E'
    D ='D'
    C = 'C'
    B = 'B'
    A = 'A'
    Aplus = 'A+'
    ADpoblePluse =  'A++'

class PropertyData(BaseModel):  

    zip_code : Optional[int] = 0
    total_area_sqm :  Optional[float] = 0
    surface_land_sqm: float
    nbr_frontages : Optional[int] = 0
    nbr_bedrooms: int
    terrace_sqm :  Optional[int] = 0
    garden_sqm :  Optional[int] = 0
    property_type : PropertyType
    state_building :  BuildingState  
    heating_type: HeatingType
    province : Province
    epc: EPC   
   



@app.get("/")
async def root():
    """Route that return 'Alive!' if the server runs."""
    return {"Status": "Alive!"}


@app.post("/predict")
async def predict(propertyData : PropertyData):
    """Route that do preprocessing data and predict property price"""
    try:
        new_data = propertyData.model_dump()
        preprocessor = PreprocesseData(new_data)
        prediction = preprocessor.preprocess_data()
        print (prediction)
        return {"prediction": float(prediction[0])}

    except ValidationError as e:
         # Custom error handling for validation errors
        custom_errors = []
        for error in e.errors():
            field = "->".join(map(str, error['loc']))
            custom_message = f"Error in field '{field}': {error['msg']}"
            custom_errors.append({"field": field, "message": custom_message})
        raise HTTPException(status_code=422, detail=custom_errors)
    except TypeError as e:
        print(f"TypeError: {e}")
    except Exception as e:
        # Handle unexpected errors
        raise HTTPException(status_code=500, detail=str(e))
