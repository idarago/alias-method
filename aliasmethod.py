import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class AliasMethod:
    def __init__(self, dist):
        self.dist = dist
        self.createAlias() # Initializes the prob and alias tables

    def createAlias(self):
        n = len(self.dist)
        self.prob = {}
        self.alias = {}
        
        small, large = [], []
        for x in self.dist:
            self.prob[x] = n * self.dist[x]
            if self.prob[x] < 1:
                small.append(x)
            else:
                large.append(x)

        while small and large:
            s = small.pop()
            l = large.pop()

            self.alias[s] = l

            self.prob[l] = (self.prob[l] + self.prob[s]) - 1

            if self.prob[l] < 1:
                small.append(l)
            else:
                large.append(l)

        while large:
            self.prob[large.pop()] = 1
        while small:
            self.prob[small.pop()] = 1

    def generateRandom(self):
        rect = np.random.choice(list(self.dist.keys()))
        if self.prob[rect] >= np.random.uniform():
            return rect
        else:
            return self.alias[rect]

rng = AliasMethod({'A':0.6,'B':0.20,'C':0.15,'D':0.05})
experiments = 10000
results = [rng.generateRandom() for _ in range(experiments)]
from collections import Counter
print(Counter(results))
sns.countplot(results, order=["A","B","C","D"])
plt.show()