# -*- coding: utf-8 -*-
"""
Created on Mon May 15 08:52:21 2023

@author: ccomb

"""
import scipy.stats as stats
import numpy as np
from math import pi 
from matplotlib import pyplot as plt

sigma=np.array([[0.5,0.25] ,[0.25,0.5]])  #on choisit la matrice de covariance
mu=np.array([3 ,2]) #on choisit le centre de l'ellipse
z = stats.multivariate_normal.rvs(mu,sigma,1000) #on génère les points aléatoires selon la loi normale bidimensionnelle

plt.scatter (z [: ,0] , z [: ,1] , edgecolors ="black") #on affiche les points aléatoires
lambdas,vecs=np.linalg.eig(sigma) #on calcule les valeurs propres et les vecteurs propres de la matrice de covariance
lambda1=lambdas[0] 
lambda2=lambdas[1]
theta=np.arccos(vecs[0][0]) #on calcule l'angle de rotation de l'ellipse

K_99=(0.01)/(2*pi*np.sqrt(lambda1*lambda2)) #on calcule les valeurs de K pour différentes probabilités
K_95=(0.05)/(2*pi*np.sqrt(lambda1*lambda2))
K_50=(0.5)/(2*pi*np.sqrt(lambda1*lambda2))
K_05=(0.95)/(2*pi*np.sqrt(lambda1*lambda2))
K=[K_99,K_95,K_50,K_05]
for i in range(4) :
    a=np.sqrt((2*lambda1*np.log((1/(2*pi*K[i]*np.sqrt(lambda1*lambda2)))))) #on calcule les demi-axes de l'ellipse
    b=np.sqrt((2*lambda2*np.log((1/(2*pi*K[i]*np.sqrt(lambda1*lambda2))))))
    t=np.linspace(0,2*pi,1000) #on crée un vecteur de 1000 points entre 0 et 2pi
    plt.plot(mu[0]+a*np.cos(theta)*np.cos(t)-b*np.sin(theta)*np.sin(t),
             mu[1]+a*np.sin(theta)*np.cos(t)+b*np.cos(theta)*np.sin(t),"red")

plt.grid(color='lightgray',linestyle='--')
plt.show()