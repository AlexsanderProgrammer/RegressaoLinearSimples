# -*- coding: utf-8 -*-
"""Regressão Linear Simples.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10995Qal3X9ep3cqKoCfX5f_2KmuUScPE
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression

# Amostra Randômica com o make_regression
x,y = make_regression(n_samples=200, n_features=1, noise=30)

plt.scatter(x,y)

#Treinando o modelo com base nos dados gerados

modelo = LinearRegression()
modelo.fit(x,y)

a_coeff = modelo.coef_ #Coeficiente Angular
l_coeff = modelo.intercept_ #Coeficiente linear

print('Coeficiente Angular: {0}\nCoeficiente Linear: {1}'.format(a_coeff,l_coeff))

plt.scatter(x,y)
plt.plot(x, l_coeff + a_coeff * x, color='red')
plt.show