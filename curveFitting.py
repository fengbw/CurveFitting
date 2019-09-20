import numpy as np
import math

class curveFitting():
    def __init__(self, x, t, m):
        self.a = 0.005
        self.b = 11.1
        self.M = m
        self.N = len(x)
        self.x = x
        self.t = t
        self.S = None
        self.getS()

    def phi(self, x):
        phi = np.zeros((self.M + 1, 1), float)
        for i in range(self.M):
            phi[i][0] = math.pow(x, i)
        return phi

    def getS(self):
        sum = np.zeros((self.M + 1, self.M + 1), float)
        for i in range(self.N):
            phiVal = self.phi(self.x[i])
            sum = np.add(sum, np.dot(phiVal, phiVal.T))
        sum = self.b * sum
        self.S = np.linalg.inv(np.identity(self.M + 1) * self.a + sum)

    def getS2(self, x):
        s = np.dot(self.phi(x).T, np.dot(self.S, self.phi(x)))
        sVal = s[0][0]
        s2x = 1 / self.b + sVal
        return s2x

    def getMx(self, x):
        sum = np.zeros((self.M + 1, 1), float)
        for i in range(self.N):
            phiVal = self.phi(self.x[i])
            sum = np.add(sum, np.dot(phiVal, self.t[i]))
        mx = self.b * self.phi(x).T
        mx = np.dot(mx, self.S)
        mx = np.dot(mx, sum)
        return mx[0][0]
