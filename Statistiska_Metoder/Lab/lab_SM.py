import numpy as np
import scipy.stats as stats

class LinearRegression: 
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    @property
    def confidence_level(self):
        return self._confidence_level

    @property
    def confidence_level(self):
        conf_level = self.relevance()
        return conf_level

    @property
    def alpha(self):
        return 1 - self.confidence_level
    
    @property
    def B(self):
        return np.linalg.pinv(self.X.T @ self.X) @ self.X.T @ self.Y

    @property
    def n(self):
        return self.Y.shape[0]
    
    @property
    def d(self):
        return len(self.B)-1
    
    def SSE(self):
        return np.sum(np.square(self.Y - (self.X @ self.B)))
    
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
        for i in range(len(self.B)):
            if i == 0:
                continue
            sig_statistic = self.B[i] / (self.std_dev()*np.sqrt(c[i,i]))
            p_value = 2*min(stats.t.cdf(sig_statistic, self.n-self.d-1), stats.t.sf(sig_statistic, self.n-self.d-1))
            p_value_list.append(p_value)
        return p_value_list

    def pearsonr(self):
        X = self.X[:,1:]
        return [(i, j, stats.pearsonr(X[:,i], X[:,j])[0]) for i in range(X.shape[1]) for j in range(i + 1, X.shape[1])]

    def confidence_interval(self):
        t_critical = stats.t.ppf(1 - self.alpha / 2, self.n - self.d - 1)
        ci = []
        for i in range(len(self.B)):
            margin_of_error = t_critical * (self.std_dev() * np.sqrt(np.linalg.pinv(self.X.T @ self.X)[i, i]))
            lower = self.B[i] - margin_of_error
            higher = self.B[i] + margin_of_error
            ci.append((lower, higher))
        return ci