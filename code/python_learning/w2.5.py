import numpy as np

def load_california_data():
    from sklearn.datasets import fetch_california_housing
    data = fetch_california_housing()
    X, y = data.data, data.target
    return X, y

def preprocess_data(X, y, test_size=0.2, random_state=10000):
    # 随机排列
    np.random.seed(random_state)
    X = np.concatenate([np.ones((X.shape[0], 1)), X], axis=1)
    indices = np.random.permutation(X.shape[0])
    # 划分训练集测试集
    test_size = int(X.shape[0] * test_size)
    X_train, X_test = X[indices[:-test_size]], X[indices[-test_size:]]
    y_train, y_test = y[indices[:-test_size]], y[indices[-test_size:]]
    return X_train, X_test, y_train, y_test


class LinearRegression:
    def __init__(self):
        self.mdl_ = None

    def fit_analytical(self, X, y):
        # 解析解
        self.mdl_ = np.linalg.inv(X.T @ X) @ X.T @ y

    def fit_gradient_descent(self, X, y, learning_rate=0.0001, n_iterations=100000):
        # 梯度下降
        n_samples, n_features = X.shape
        self.mdl_ = np.zeros(n_features)
        for k in range(n_iterations):
            # 梯度裁剪
            clip_threshold = 0.5
            gradients = -(2 / n_samples) * X.T @ (y - X @ self.mdl_)
            if clip_threshold:
               gradients = np.clip(gradients, -clip_threshold, clip_threshold)
            self.mdl_ -= learning_rate * gradients

    def predict(self, X):
        return X @ self.mdl_



X, y = load_california_data()

X_train, X_test, y_train, y_test = preprocess_data(X, y)

# 实例化
analytical = LinearRegression()
gradient_descent = LinearRegression()

# 模型训练
analytical.fit_analytical(X_train, y_train)
gradient_descent.fit_gradient_descent(X_train, y_train)

# 在测试集上进行预测
y_predict_analytical = analytical.predict(X_test)
y_predict_gradient_descent = gradient_descent.predict(X_test)

# 计算MSE
mse_analytical = np.mean((y_test - y_predict_analytical) ** 2)
mse_gradient_descent = np.mean((y_test - y_predict_gradient_descent) ** 2)

print("MSE (Analytical Solution):", mse_analytical)
print("MSE (Gradient Descent):", mse_gradient_descent)

