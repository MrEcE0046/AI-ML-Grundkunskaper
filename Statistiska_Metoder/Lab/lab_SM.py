import numpy as np
import scipy.stats as stats

class LinearRegression: 

    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        alpha = 0.05
        confidence_level = 0.95

    @property
    def b(self):
        return np.linalg.pinv(self.X.T @ self.X) @ self.X.T @ self.Y

    @property
    def n(self):
        return self.Y.shape[0]
    
    @property
    def d(self):
        return len(self.b)-1
    
    @property
    def confidence_level(self):
        pass
    
    def SSE(self):
        return np.sum(np.square(self.Y - (self.X @ self.b)))
    
    def SSR(self):
        return self.Syy() - self.SSE()
    
    def Syy(self):
        return (self.n*np.sum(np.square(self.Y)) - np.square(np.sum(self.Y)))/self.n
        # return np.sum((self.Y - np.mean(self.Y))**2)

    def var(self):
        # A function or method to calculate the variance.
        return self.SSE() / (self.n-self.d-1)

    def std_dev(self): # = S
        # A function or method to calculate the standard deviation.
        # return np.std(self.Y)
        return np.sqrt(self.var())

    def significance_regression(self):
        # A function or method to calculate the significance of the regression.
        sig_statistics = (self.SSR() / self.d)/self.std_dev() # Ska vara std_dev istället för var
        p_significance = stats.f.sf(sig_statistics, self.d, self.n-self.d-1)
        return p_significance

    def relevance(self):
        # A function or method that reports the relevance of the regression (R2).
        return self.SSR() / self.Syy()
    
    def significance(self):
        c = np.linalg.pinv(self.X.T@self.X)*self.var()
        p_value_list = []
        for i in range(len(self.b)):
            if i == 0:
                continue
            sig_statistic = self.b[i] / (self.std_dev()*np.sqrt(c[i,i]))
            p_value = 2*min(stats.t.cdf(sig_statistic, self.n-self.d-1), stats.t.sf(sig_statistic, self.n-self.d-1))
            p_value_list.append(p_value)
        return p_value_list

    def pearsonr(self):
        X = self.X[:,1:]
        return [(i, j, stats.pearsonr(X[:,i], X[:,j])[0]) for i in range(X.shape[1]) for j in range(i + 1, X.shape[1])]

    def confidence_interval(self):
        

















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