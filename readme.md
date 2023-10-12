## REST API for predicting WOZ value

This REST API is designed to predict the WOZvalue based on input parameters. The model used by the API is trained using machine learning techniques and saved as a binary file for quick access.

#### Prerequisites
Python 3.x
Flask
Numpy
Scikit-Learn
Joblib
Docker

#### Installation
1. Clone this repository to your local machine.
2. Open a terminal or command prompt and navigate to the directory where you cloned the repository.
3. Install the required packages:
`pip install-r requirements.txt`

#### USAGE 


1. Choose your method of execution Flask/Docker
###### By FLASK
Start the Flask server by executing:
`python restapi.py`

OR 

###### By DOCKER
Prerequisite - Make sure Docker Engine is running. 
Build the Docker image using the Dockerfile provided in the repository:
code:
`docker build -t woz_api .`

Run the Docker container:
code:
`docker run -p 5000:5000 -t -i woz_api`

This will start the Docker container and bind port 5000 of the container to port 5000 of your host machine.


2. Access the API by visiting the following URL in your web browser.
Send a GET request to the API endpoint to get a WOZ value prediction. The input parameters should be included in the URL query string in the format :-
`
http://localhost:5000/api/get_woz_value?parameter1=<single>&parameter2=<married, no kids>&parameter3=<not married, no kids>&parameter4=<married, with kid>&parameter5=<not married, with kids>&parameter6=<single parent>&parameter7=<other>&parameter8=<total>`


example Url:- 
http://localhost:5000/api/get_woz_value?parameter1=%22A00a%20Kop%20Zeedijk%22&parameter2=543.0&parameter3=37.0&parameter4=149.0&parameter5=14.0&parameter6=12.0&parameter7=22.0&parameter8=12.0&parameter9=789.0
"
3. The API will return a JSON object with the predicted WOZ value:
example:
{
    "woz_value": 456789.456
}
4. To stop the server, press Ctrl + C in the terminal or command prompt.

Note: If you are running Docker on a virtual machine or on a remote server, replace localhost with the IP address of the machine running Docker.


### Development
To update the training job, you may update src. It involves reading data,preprocessing,  splitting it into train and test sets, standardizing the data, applying principal component analysis (PCA), training the model with hyperparameter tuning using the PCA-transformed training set, and evaluating the trained model on the test set. The process assumes the existence of a Preprocessor class with methods to split, scale, and apply PCA to data, as well as a train_model function and an evaluate_model function.

Wrapper-  Trainer.py
execution - python trainer.py 

sample output
```
PS C:\Users\purvi\Documents\Xomnia Assessment> python trainer.py   
2023-04-21 14:48:06,038 - __main__ - INFO - Reading data...
2023-04-21 14:48:06,931 - __main__ - INFO - Splitting data into train and test sets...
2023-04-21 14:48:06,946 - __main__ - INFO - Standardizing data...
2023-04-21 14:48:06,957 - __main__ - INFO - Applying PCA...
2023-04-21 14:48:07,021 - __main__ - INFO - Training model...
2023-04-21 14:49:37,463 - __main__ - INFO - Evaluating model...
Mean Squared Error: 31560132655.26716
R2 Score: 0.39810779884699758

```   

### Conclusion
This project demonstrates how to build and deploy a machine learning model as a REST API using Flask. The prediction model is trained on a dataset of house parameters and WOZ values and can be used to predict the WOZ value of a house based on its parameters. The project also includes visualizations and statistics for data exploration and Dockerized script for for model training and development.
The solution is packaged to be deployed as a webservice for third party applications.


#### Additional Information
The trained machine learning model used by the API is saved in a binary file named model.joblib in the code folder.
The scaler and PCA objects used to transform the input data are saved as joblib files named scaler.joblib and pca.joblib, respectively in the code folder.