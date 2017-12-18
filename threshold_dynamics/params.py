import numpy as np


class Params:
    def __init__(self,
                 xgraph1=None, xgraph2=None, xgraph3=None, xgraph4=None, xgraph5=None,
                 foo=None, mu=None, sigma=None, alpha=None, beta=None,
                 a1=None, b1=None,
                 a2=None, b2=None,
                 a3=None, b3=None):

        self.xgraph1 = xgraph1
        self.xgraph2 = xgraph2
        self.xgraph3 = xgraph3
        self.xgraph4 = xgraph4
        self.xgraph5 = xgraph5
        self.ygraph1 = np.array([])
        self.ygraph2 = np.array([])
        self.ygraph3 = np.array([])
        self.ygraph4 = np.array([])
        self.ygraph5 = np.array([])
        self.xgraphs = [self.xgraph1, self.xgraph2, self.xgraph3, self.xgraph4, self.xgraph5]
        self.ygraphs = [self.ygraph1, self.ygraph2, self.ygraph3, self.xgraph4, self.xgraph5]
        self.foo = foo
        self.mu = mu
        self.sigma = sigma
        self.alpha = alpha
        self.beta = beta
        self.a1 = a1
        self.b1 = b1
        self.a2 = a2
        self.b2 = b2
        self.a3 = a3
        self.b3 = b3
        self.params = [self.a1, self.b1, self.a2, self.b2, self.a3, self.b3]
