import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
import pickle

class Perceptron:
    def __init__(self, eta:float =0.01, n_iter:int =10):
        self.eta = eta
        self.n_iter = n_iter
    
    def fit(self, X: pd.DataFrame, Y: pd.DataFrame):
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X,Y):
                update=self.eta*(target-self.predict(xi))
                self.w_[1:] += update *xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self
    
    
    def net_input(self, X: pd.DataFrame):
        return np.dot(X, self.w_[1:]) + self.w_[0]
    
    def predict(self, X: pd.DataFrame):
        return np.where(self.net_input(X) >= 0, 1, -1)

iris_df = load_iris()

df = pd.DataFrame(data = np.c_[iris_df["data"], iris_df["target"]], columns = iris_df["feature_names"]+["target"])
df.drop(df.index[df["target"] == 2], inplace = True)
X = df.loc[:, ["petal length (cm)", "sepal length (cm)"]].values
Y = df.loc[:, ["target"]].values
model = Perceptron()
model.fit(X, Y)

with open("perceptron.pkl", "wb") as md:
    pickle.dump(model, md)




