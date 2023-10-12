import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from joblib import dump
import logging

# Reads project's classes
from src.data_importer import read_data
from src.preprocessor import Preprocessor
from src.train_model import train_model
from src.evaluate_model import evaluate_model



# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create console handler and set level to info
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)


# read the data
logger.info('Reading data...')
df = read_data()
 
# split data into train and test sets
logger.info('Splitting data into train and test sets...')
X_train, X_test, y_train, y_test = Preprocessor.split_data(df)

# standardize the training and test sets
logger.info('Standardizing data...')
X_train_std, X_test_std = Preprocessor.scale_data(X_train, X_test)

# apply PCA to the standardized training and test sets
logger.info('Applying PCA...')
X_train_pca, X_test_pca = Preprocessor.apply_pca(X_train_std, X_test_std)

# train the model using the PCA-transformed training set and perform grid search for hyperparameter tuning
logger.info('Training model...')
model = train_model(X_train_pca, y_train)

# evaluate the trained model on the test set
logger.info('Evaluating model...')
evaluate_model(X_test_pca, y_test)
