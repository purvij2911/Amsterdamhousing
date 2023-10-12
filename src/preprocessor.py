from joblib import dump
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

class Preprocessor:

    def split_data(df):
        # Split into training and test sets
        X = df.drop(['area', 'average woz value'], axis=1)
        y = df['average woz value']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        return X_train, X_test, y_train, y_test


    def scale_data(X_train, X_test):
        # Standardize the training and test sets
        scaler = StandardScaler()
        X_train_std = scaler.fit_transform(X_train)
        X_test_std = scaler.transform(X_test)

        # Save the scaler object
        dump(scaler, 'code/scaler.joblib')

        return X_train_std, X_test_std


    def apply_pca(X_train_std, X_test_std):
    # Apply PCA to the training set to get the best number of components
        pca = PCA()
        pca.fit(X_train_std)
        pca_cumulative_var_ratio = pca.explained_variance_ratio_.cumsum()
        num_components = sum(pca_cumulative_var_ratio < 0.95) + 1
        pca = PCA(n_components=num_components)
        X_train_pca = pca.fit_transform(X_train_std)
        X_test_pca = pca.transform(X_test_std)

        # Save the pca object
        dump(pca, 'code/pca.joblib')

        return(X_train_pca,X_test_pca)
