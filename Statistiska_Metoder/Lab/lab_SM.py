import numpy as np
import scipy.stats as stats

class LinearRegression: 

    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    @property
    def b(self):
        return np.linalg.pinv(self.X.T @ self.X) @ self.X.T @ self.Y

    @property
    def n(self):
        return self.Y.shape[0]
    
    @property
    def d(self):
        return len(self.b)-1
    
    def SSE(self):
        return np.sum(np.square(self.Y - (self.X @ self.b)))
    
    def SSR(self):
        return np.sum(((self.X @ self.b) - np.mean(self.Y))**2)
    
    def SST(self):
        return np.sum((self.Y - np.mean(self.Y))**2)

    def var(self):
        # A function or method to calculate the variance.
        var = self.SSE() / (self.n-self.d-1)
        return var

    def std_dev(self):
        # A function or method to calculate the standard deviation.
        # std_dev = np.std(self.Y)
        std_dev = np.sqrt(self.var())
        return std_dev

    def significance_regression(self):
        # A function or method to calculate the significance of the regression.
        S = np.sqrt(self.var())
        sig_statistics = (self.SSR() / self.d)/S
        p_significance = stats.f.sf(sig_statistics, self.d, self.n-self.d-1)
        return p_significance

    def relevance(self):
        # A function or method that reports the relevance of the regression (R2).
        R2 = self.SSR() / self.SST()
        return R2
























       # def __init(self, ls):
    #     assert len(ls) == 2
    #     self.real = self.imag = ls

    # def __inti__(self, real, imag):
    #     self.real = real
    #     self.imag = imag 

    # def __repr__(self):
    #     return f"{repr(self.real)} + {repr(self.imag)}i"
    
    # def __add__(self, other):
    #     return complex(self.real + other.real, self.imag + other.imag)
    
    # def fit(X, y):
    #     b = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
    #     return b

    # Aproperty "d" that contains the number of features/parameters/dimensions of the model.
    # Aproperty n that contains the size of the sample.