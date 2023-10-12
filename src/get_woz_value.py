import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


# Load the trained model from disk
model = joblib.load('code/model.joblib')

# Load saved scaler and PCA objects
scaler = joblib.load('code/scaler.joblib')
pca = joblib.load('code/pca.joblib')
    
# Function to transform new data using saved scaler and PCA objects
def transform_data(data):
    #removing area and total as it was not used when building the model
    input_data = data[:, 1:-1]
    input_data = input_data.astype(float)
    # Scale data
    scaled_data = scaler.transform(input_data)
    # Apply PCA transform
    transformed_data = pca.transform(scaled_data)
    return transformed_data

#Transform the woz_value to actual value
#def transform_woz(woz_value_log):
#    woz_value = np.exp(woz_value_log)
#    return woz_value

def get_woz_value(parameter1, parameter2, parameter3, parameter4, parameter5, parameter6, parameter7, parameter8, parameter9):
    # Transform input parameters into numpy array
    input_data = np.array([parameter1, parameter2, parameter3, parameter4, parameter5, parameter6, parameter7, parameter8,parameter9]).reshape(1, -1)
    
    #Transforming input data as model data
    transformed_data = transform_data(input_data)

    # Use the model to make a prediction
    woz_value = model.predict(transformed_data)[0]
    
    #transform the output to woz_value
#    woz_value = transform_woz(woz_value_log)

    # Create a dictionary with the result
    result = {'woz_value': woz_value}
    print(result)
    return result
