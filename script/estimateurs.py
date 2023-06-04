import scipy.stats as stats
import numpy as np
from math import pi 
from math import sqrt
from matplotlib import pyplot as plt
from random import *

#Statistiques 
def estimateur_1_echantillon_aléatoire(nb_points,proba):
    def test_aleatoire(nb_points):
        #génère un écghantillonaléatoire pour une population de nb_points entier
        absc=randint(0,5);ordo=randint(0,5)
        sig11=randint(1,10);sig22=randint(1,10)
        sig12=sigma11=randint(0,10)
        z=stats.multivariate_normal.rvs([absc ,ordo],
                             [[sig11,sig12],[sig12,sig22]],nb_points)
        plt.scatter(z[:,0],z[:,1] , edgecolors ="black")
        return(z)  
    def printellipse(K,lambda1,lambda2,X0,Y0):
        a=np.sqrt(np.abs(2*lambda1*np.log(np.abs(2*pi*K*np.sqrt(lambda1*lambda2)))))
        b=np.sqrt(np.abs(2*lambda2*np.log(np.abs(2*pi*K*np.sqrt(lambda1*lambda2)))))
        theta=np.arccos(vecs[0][0])
        t = np.linspace(0,2*pi,200)
        plt.plot( mu[0]+a*np.cos(theta)*np.cos(t)-b*np.sin(theta)*np.sin(t) , 
                 mu[1]+a*np.sin(theta)*np.cos(t)+b*np.cos(theta)*np.sin(t),".")
        
    #génération d'un échantillon aléatoire
    z=test_aleatoire(nb_points)
    N=len(z[:,0])
    
    #construction de l'estimateur du centre de l'échantillon
    S=sum(z);  X=S[0]/N ;  Y=S[1]/N;  mu=[X,Y]
    
    #construction de l'estimateur de la matrice de covarience 
    sig11=0; sig12=0; sig22=0
    for i in range(N):
        sig11+= (z[i,0]-X)**2 
        sig22+= (z[i,1]-Y)**2
        sig12+= (z[i,0]-X)*(z[i,1]-Y) 
    sig11=sig11/(N-1); sig22=sig22/(N-1); sig12=sig12/(N-1)
    sigma=[[sig11,sig12] , [sig12,sig22]]
    
    #parametres de léchantillon solon en
    #vue de modéliser une loi normale bidimentionnelle 
    lambdas,vecs=np.linalg.eig(sigma)
    lambda1=lambdas[0]; lambda2=lambdas[1]
    theta=np.arccos(vecs[0][0])
    
    #Construction d'une ellipse d'isodensité K sensée contenir (proba*100)%  
    #des valeurs de l'échantillon  
    K=(1-proba)/(2*pi*sqrt(lambda1*lambda2))
    printellipse(K,lambda1,lambda2,mu[0],mu[1])
    
    #Construction d'une ellipse d'isodensité K sensée contenir ((proba/2)*100)%  
    #des valeurs de l'échantillon
    K=(1-(proba/2))/(2*pi*sqrt(lambda1*lambda2))
    printellipse(K,lambda1,lambda2,mu[0],mu[1])
    
    #Construction d'une ellipse d'isodensité K sensée contenir ((proba/4)*100)%  
    #des valeurs de l'échantillon
    K=(1-(proba/4))/(2*pi*sqrt(lambda1*lambda2))
    printellipse(K,lambda1,lambda2,mu[0],mu[1])
    return(mu,sigma)
mu,sigma=estimateur_1_echantillon_aléatoire(1000,0.99)
print(mu)
print(sigma)
