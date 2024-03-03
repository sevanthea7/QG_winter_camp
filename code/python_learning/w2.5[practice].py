import numpy as np

def load_housing_data():
    from sklearn.datasets import fetch_california_housing
    data = fetch_california_housing()
    X, y = data.data, data.target
    return X, y

def preprocess_data(X, y, test_size=0.2, random_state=42):
    np.random.seed(random_state)
    X = np.concatenate([np.ones((X.shape[0], 1)), X], axis=1)
    random_queue = np.random.permutation(X.shape[0])
    test_size = int(X.shape[0] * test_size)
    X_train, X_test = X[random_queue[:-test_size]], X[random_queue[-test_size:]]
    y_train, y_test = y[random_queue[:-test_size]], y[random_queue[-test_size:]]
    return X_train, X_test, y_train, y_test

class LR:
    def __init__(self):
        self.mdl = None

    def fit_anal(self, X, y):
        self.mdl = np.linalg.inv(X.T @ X) @ X.T @ y

    def fit_gd(self, X, y, rate=0.001, rounds = 1000):
        samples, features = X.shape
        self.mdl = np.zeros(features)
        for i in range(rounds):
            gradients = -(2 / samples) * X.T @ (y - X @ self.mdl)
            self.mdl -= rate * gradients

    def predict(self, X):
        return X @ self.mdl


X, y = load_housing_data()

X_train, X_test, y_train, y_test = preprocess_data(X, y)

mdl_anal = LR()
mdl_gd = LR()

mdl_anal.fit_anal(X_train, y_train)
mdl_gd.fit_gd(X_train, y_train)

prd_anal = mdl_anal.predict(X_test)
prd_gd = mdl_gd.predict(X_test)

mse_anal = np.mean((y_test - prd_anal) ** 2)
mse_gd = np.mean((y_test - prd_gd) ** 2)

print('MSE_ANALYTICAL: ', mse_anal)
print('MSE_GD: ', mse_gd)


