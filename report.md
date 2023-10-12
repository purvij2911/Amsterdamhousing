# WOZ Value Prediction Model and REST API


### Problem Statement
The Municipality needs to predict the average WOZ value of houses based on family composition. This prediction model will be used as an indicator for house valuation by other governments and real estate agencies.

#### TASKS
1. Build a prediction model that predicts the average WOZ value

2. Build a REST web service that includes all features and returns a prediction of the WOZ. 

3. Package your model REST web service into a ready to be deployed solution. 

4. Design a high-level architecture for deploying the web service on cloud taking into account the following requirements:
-   The web service should have high availability and scalability to
accommodate peaks in usage. Only authenticated clients should have access
to the service.
-   Historical & new data of daily frequency, reside/arrive as CSV files at the
object storage of the cloud environment of your choice (AWS S3/ GCP Cloud
Storage/ Azure Blob Storage). An ETL mechanism is necessary to transform
the raw form of new batches to be used for the model.
-   Cost should be kept as low as possible without impact on the requirements.
 

## My Solutions

My goal was to implement a system that would fullfil the objectives above and can be used by the municipality if needed. 

├── README.md
├── code                                             ` #this has model artifacts`
│   ├── __init__.py
│   ├── model.joblib
│   ├── job.joblib
│   ├── pca.joblib
├── data                                             `data source`
│   ├── 2021_family_composition_amsterdam.xlsx
│   └── woz_prices_2021_amsterdam.xlsx
├── EDA                                              
│   ├── EDA.ipynb
│   └── EDA_data.html
├── tests                                               `pytest script to validate output of RESTapi`
│   ├── __init__.py
│   ├── test_api.py
├── src                                                `Souce code for main functions/wrapper`
│   ├── __init__.py
│   ├── data_importer.py
│   ├── evaluate_model.py
│   ├── get_woz_value.py
│   ├── preprocessor.py
|   ├── train_model.py
├── main.py                                               `RESTapi function`
├── trainer.py                                            ` Model training wrapper`
├── requirements.txt                                      `requirement.txt for the project`
├── Dockerfile                                            `Docker file for RESTapi`
├── Architechture_diagram.html                            `Architechture Diagram for the solution on AWS`
├── ModelAnalysis.ipynb                                   `Model analysis notebook for reference`
└── report.md                                             `Elaborative Report on the project`


### Project Setup

#### Prerequisites
To run this project, you need to have the following installed on your system:

Python 3.x
pip
Docker

<b>Installation</b>
Navigate to the project directory:
`cd Xomnia Assessment`

Install the required packages:
`pip install -r requirements.txt`


#### Usage
To use the WOZ value prediction model and REST API, follow the steps below:

Start the Flask server by executing:
`python main.py`
Open a web browser and send a GET request to the following URL:
`
http://localhost:5000/api/get_woz_value?parameter1=<single>&parameter2=<married, no kids>&parameter3=<not married, no kids>&parameter4=<married, with kid>&parameter5=<not married, with kids>&parameter6=<single parent>&parameter7=<other>&parameter8=<total>
`   

Replace the parameters with the actual values for the house you want to predict the WOZ value for.

parameter1: Area within Amsterdam
parameter2: Number of single households
parameter3: Number of married households without kids
parameter4: Number of not Married households without kids
parameter5: Number of married households with kids
parameter6: Number of not married households with kids
parameter7: Number of single parent households
parameter8: Number of other types of household
parameter9: Total number of households in area

The API will return the predicted WOZ value for the house in JSON format.

OR

You can use Docker, make sure Docker is running
Build the Docker image using the Dockerfile provided in the repository:
code:
`docker build -t woz_api .`

Run the Docker container:
code:
`docker run -p 5000:5000 -t -i woz_api`

This will start the Docker container and bind port 5000 of the container to port 5000 of your host machine.

Open a web browser and send a GET request to the following URL:
`
http://localhost:5000/api/get_woz_value?parameter1=<single>&parameter2=<married, no kids>&parameter3=<not married, no kids>&parameter4=<married, with kid>&parameter5=<not married, with kids>&parameter6=<single parent>&parameter7=<other>&parameter8=<total>
`   

To stop the server, press Ctrl + C in the terminal or command prompt.


### Development


    - Data Importation:
This step involves importing the necessary data into the project using the src/data_importer.py module.

    - Exploratory Analysis:     
In this step, exploratory data analysis (EDA) is performed on the imported data using Jupyter Notebook (EDA/EDA.ipynb) and the results are saved as an HTML file (EDA/EDA_data.html).

    - ETL:
The preprocessor.py module performs the extract, transform, and load (ETL) operations on the data, including scaling and principal component analysis (PCA).

    - Model Training:
The train_model.py module is used to train the machine learning model using the preprocessed data.

    - Wrapper: 
The trainer.py function serves as a wrapper that utilizes all of the above functions and saves the trained model and other necessary artifacts to be used by the REST API.

    - Creating Rest API:
The main.py module creates a RESTful API that enables a GET method to return the "woz value" predicted by the trained model.

    - Creating Docker container:
The Dockerfile is used to package the entire solution into a container, which can be deployed to any environment.

    - Testing API: 
The test_api.py module is created to test the API, ensuring that it returns a 200 status code and that the output is a numeric value.

    - EDA
The EDA folder has two files, 
1. The EDA.html is generated by pandas_profiling for a general analysis of data on higher level
2. the python notebook is used to draw visualization on the given data the main graphs are:

            -Distribution of average woz value
            -Correlation Matrix
            -Top 10 Neighbourhood of Amsterdam
            -Distribution of Household types(single,married..)
            -Top 10 area for each household type
            -Household composition distribution per area for top 10 area
            -Household composition distribution per area for bottom 10 area
    
    
    
    - ModelAnalysis.ipynb
This notebook is used for exploring different models using cross-validation and grid search CV to find the best performing model. The different models and there scores are 

                LinearRegression
                Cross-Validation Scores: [0.24745409 0.10159848 0.20271533 0.16392079 0.23693314]
                Mean R-squared: 0.1905243683628914
                Standard Deviation: 0.05321456797002546


                Ridge
                Cross-Validation Scores: [0.24745412 0.10159848 0.20271534 0.16392077 0.23693333]
                Mean R-squared: 0.19052440774366805
                Standard Deviation: 0.053214610734211465


                Lasso
                Cross-Validation Scores: [0.2474541  0.10159848 0.20271533 0.16392079 0.23693315]
                Mean R-squared: 0.1905243703800976
                Standard Deviation: 0.05321457138491528


                RandomForestRegressor
                Cross-Validation Scores: [0.33177226 0.47804087 0.25015283 0.35595564 0.49186742]
                Mean R-squared: 0.3815578054056187
                Standard Deviation: 0.09151888436970558


                DecisionTreeRegressor
                Cross-Validation Scores: [-1.01099723  0.24440205 -0.1713168   0.34748215 -0.06259626]
                Mean R-squared: -0.1306052183903865
                Standard Deviation: 0.4797021420444285


                Best performing regressor: RandomForestRegressor
                Mean R-squared: 0.3815578054056187
                
        

#### Improvement points
1. The model is underperforming. Collecting more data can be helpful in improving the performance of the model. Additionally, ensuring that the collected data is representative of the real-world scenarios that the model will be used in is crucial.
example - Location, Property type, Property size, Age and Condition of house, Energy efficiency, Market Trends

2. Feature Engineering: Feature engineering is a crucial aspect of building a successful machine learning model. In this project, it would be beneficial to explore more features that could be engineered.

3. Model Interpretability: It is essential to understand how the model is making predictions. This can be done by exploring feature importance, partial dependence plots, and other methods for interpreting the model. Since there is limited time and data was highly correlated, PCA was used which makes the features less interpretable 

4. Its possible to improve the code by creating Containers for training process. 

5. Adding more pytest for different modules to ensure the quality of their code and catch bugs. 

6. More researched could have been put into the architecture diagram for batch inference and real time inference.

7. Lastly if time permitted, I could have consolidated a ppt explaining the project, data and visualizations and graphs.


#### Improvement steps
If you want to modify or improve the prediction model, you can follow the steps below:

Open the model_training.ipynb notebook in Jupyter Notebook or Jupyter Lab.
Modify the notebook to make changes to the model, data preprocessing, or hyperparameters.
Run the notebook to train and save the updated model, scaler, and PCA objects.
Update the model.pkl, scaler.joblib, and pca.joblib files with the new saved objects.
Start the Flask server to use the updated model for prediction.
Visualizations and Statistics
The eda.ipynb notebook contains visualizations and statistics related to the dataset used for training the prediction model. These include histograms, box plots, correlation matrix, and more. The purpose of this notebook is to explore the data and gain insights that can be useful for preprocessing and feature engineering.


### Conclusion
This project demonstrates how to build and deploy a machine learning model as a REST API using Flask. The prediction model is trained on a dataset of house parameters and WOZ values and can be used to predict the WOZ value of a house based on its parameters. The project also includes visualizations and statistics for data exploration and a Jupyter notebook for model training and development.