import streamlit as st
import requests

# Set up lists of valid options based on the Literal types
property_type_options = ["HOUSE", "APARTMENT"]
building_state_options = ["TO_RESTORE", "TO_BE_DONE_UP", "TO_RENOVATE", "JUST_RENOVATED", "GOOD", "AS_NEW"]
heating_type_options = ["CARBON", "WOOD", "PELLET", "FUELOIL", "GAS", "ELECTRIC", "SOLAR"]
province_options = [
    "Antwerp", "Brussels", "East Flanders", "Flemish Brabant", "Hainaut", 
    "Limburg", "Liège", "Luxembourg", "Namur", "Walloon Brabant", "West Flanders"
]

# Streamlit app title with a house icon
st.markdown("<h1 style='text-align: center;'>🏠 Property Price Prediction</h1>", unsafe_allow_html=True)

# Input form with icons
st.subheader("🏡 Enter Property Details")
property_type = st.selectbox("🏘️ Property Type", property_type_options)
zip_code = st.number_input("📍 Zip Code", min_value=1000, max_value=9999, value=9000)
surface_land_sqm = st.number_input("📏 Surface Land (sqm)", min_value=0.0, value=200.0)
total_area_sqm = st.number_input("🏢 Total Area (sqm)", min_value=0.0, value=0.0)
nbr_frontages = st.number_input("🔲 Number of Frontages", min_value=0, value=2)
nbr_bedrooms = st.number_input("🛏️ Number of Bedrooms", min_value=1, value=3)
province = st.selectbox("🌍 Province", province_options)
terrace_sqm = st.number_input("🏖️ Terrace Area (sqm)", min_value=0, value=0)
garden_sqm = st.number_input("🌳 Garden Area (sqm)", min_value=0, value=0)
state_building = st.selectbox("🏗️ Building State", building_state_options)
heating_type = st.selectbox("🔥 Heating Type", heating_type_options)
primary_energy_consumption_sqm = st.number_input("🏖️ Energy consumption", min_value=0, value=220)


# API request
if st.button("Predict Price"):
    api_url = "https://immo-eliza-deployment-1-6o7p.onrender.com/predict"  
    data = {
        "zip_code": zip_code,
        "total_area_sqm": total_area_sqm,
        "surface_land_sqm": surface_land_sqm,
        "nbr_frontages": nbr_frontages,
        "nbr_bedrooms": nbr_bedrooms,
        "terrace_sqm": terrace_sqm,
        "garden_sqm": garden_sqm,
         "primary_energy_consumption_sqm" : primary_energy_consumption_sqm,
        "property_type": property_type,
        "state_building": state_building,
        "heating_type": heating_type,
        "province": province
    }
    response = requests.post(api_url, json=data)
    if response.status_code == 200:
        prediction = response.json().get("prediction")
        st.success(f"Predicted Price: {prediction}")
    else:
        st.error("Error occurred in prediction. Please try again.")
