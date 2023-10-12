from sklearn.metrics import mean_squared_error, r2_score
from joblib import load

def evaluate_model(X_test_pca, y_test):
    # Loading the saved model
    model = load('code/model.joblib')

    # Evaluating the model on the test set
    y_pred = model.predict(X_test_pca)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("Mean Squared Error:", mse)
    print("R2 Score:", r2)
