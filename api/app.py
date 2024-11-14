from fastapi import FastAPI, HTTPException
import os
from pydantic import BaseModel, ValidationError
from predict import PreprocesseData
from typing import Literal, Optional


# Set port to the env variable PORT to make it easy to choose the port on the server
# If the Port env variable is not set, use port 8000
PORT = os.environ.get("PORT", 8000)
app = FastAPI(port=PORT)


PropertyType = Literal["HOUSE", "APARTMENT"]
BuildingState = Literal["TO_RESTORE", "TO_BE_DONE_UP", "TO_RENOVATE", "JUST_RENOVATED", "GOOD", "AS_NEW"]
HeatingType = Literal["CARBON", "WOOD", "PELLET", "FUELOIL", "GAS", "ELECTRIC", "SOLAR"]
Province = Literal[
    "Antwerp", "Brussels", "East Flanders", "Flemish Brabant", "Hainaut", "Limburg", 
    "Liège", "Luxembourg", "Namur", "Walloon Brabant", "West Flanders"
]

class PropertyData(BaseModel):  

    zip_code : Optional[int] = 0
    total_area_sqm :  Optional[float] = 0
    surface_land_sqm: float
    nbr_frontages : Optional[int] = 0
    nbr_bedrooms: int
    terrace_sqm :  Optional[int] = 0
    garden_sqm :  Optional[int] = 0
    primary_energy_consumption_sqm :  Optional[float] = 220
    property_type : PropertyType
    state_building :  BuildingState  
    heating_type: HeatingType
    province : Province

   

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
        return {"prediction": f"{float(prediction[0]):.2f} €"}

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
