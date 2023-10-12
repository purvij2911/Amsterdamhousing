from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from joblib import dump

def train_model(X_train_pca, y_train):
    # Creating a random forest regressor and performing grid search to find the best hyperparameters
    model = RandomForestRegressor()
    param_grid = {'n_estimators': [100, 200, 300],
              'max_depth': [None, 5, 10],
              'min_samples_split': [2, 5, 10],
              'min_samples_leaf': [1, 2, 4]}
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5)
    grid_search.fit(X_train_pca, y_train)

    # Saving the model
    dump(grid_search.best_estimator_, 'code/model.joblib')
    
    return grid_search.best_estimator_
