import pandas as pd
import joblib


class  PreprocesseData:   

    def __init__(self, new_data):
        self.dataset = pd.DataFrame([new_data])
  
    def preprocess_data(self):
        
        input_df = self.dataset
        new_data = preprocess_Categorical_data(input_df)
      
        # Path to the saved xgb_regressor model
        # Load the trained xgb_regressor model 
        model_path = 'xgb_model.joblib'   
        model = load_model(model_path)

        # Make predictions on the new data 
        predictions = make_predictions(model, new_data)        
        return  predictions


def preprocess_Categorical_data(input_df):
    #encode province column
    all_provinces = ['province_Antwerp', 'province_Brussels', 'province_East Flanders',
                    'province_Flemish Brabant', 'province_Hainaut', 
                    'province_Limburg', 'province_Liège','province_Luxembourg', 
                    'province_Namur', 'province_Walloon Brabant', 'province_West Flanders']
    

    # Initialize province columns to 0
    for province in all_provinces:
        input_df[province] = 0  

    if 'province' in input_df.columns:
        input_df['province'] = input_df['province'].str.lower()
        for index, row in input_df.iterrows():
            province_col = f"province{row['province']}"
            if province_col in all_provinces:
                input_df.at[index, province_col] = 1
        input_df.drop('province', axis=1, inplace=True)

    # Apply manual encoding 
    # Mappings for 'state_building' , 'property_type' and 'epc' categories 
    property_type_mapping = {
        'HOUSE': 1, 'APARTMENT': 0}
  
    state_building_mapping = {
        'TO_RESTORE': 0, 'TO_BE_DONE_UP': 1, 'TO_RENOVATE': 2,
        'JUST_RENOVATED': 3, 'GOOD': 4, 'AS_NEW': 5
    }

    energy_mapping = {
        'CARBON': 0, 'WOOD': 1,
        'PELLET': 2, 'FUELOIL': 3,
        'GAS': 4, 'ELECTRIC': 5,'SOLAR': 6,
        }


    if 'property_type' in input_df.columns:
        input_df['property_type'] = input_df['property_type'].map(property_type_mapping).fillna(-1)
  
    if 'state_building' in input_df.columns:
        input_df['state_building'] = input_df['state_building'].map(
            state_building_mapping).fillna(-1)

    if 'heating_type' in input_df.columns:
        input_df['heating_type'] = input_df['heating_type'].map(
            energy_mapping).fillna(-1)


    return input_df

def load_model(model_path):
    #Load the trained xgb_regressor model
    return joblib.load(model_path)

def make_predictions(model, new_data):
    #Make predictions using the loaded model    
    predictions = model.predict(new_data)   
    return predictions
