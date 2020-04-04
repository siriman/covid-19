import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from statsmodels.tsa.holtwinters import SimpleExpSmoothing, Holt
import numpy as np
from sklearn.metrics import mean_squared_error
from model_covid19 import *
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import warnings
warnings.filterwarnings("ignore")

#################################################fonction bt*ln(1+at)######################################        
def func_ln(a,b,t):
    y=a*t*np.log(1+b*t)
    return  y
#############################################charger les données####################################   
def input_data(path):
    cov=pd.read_csv(path)
    return cov    
##########################################estimer parametre a et b de la fonction bt*ln(1+at) ##########################################
def estimate_ln_params(data):
    temps=data.index
    value_poss=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    mse_list=[]
    params=[]
    for i in value_poss:
        for j in value_poss:
            predict=func_ln(i,j,temps)
            error = mean_squared_error(data, predict)
            mse_list.append(error)
            params.append((i,j))
    ind=mse_list.index(min(mse_list))
    return params[ind]

##########################################estimer parametres holt linéaire ##########################################
def estimate_holt_lineaire(data):
    value_poss=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    mse_list=[]
    params=[]
    for i in value_poss:
        for j in value_poss:
            fit = Holt(data).fit(smoothing_level=i, smoothing_slope=j)
            predicted=fit.fittedvalues
            error = mean_squared_error(data, predicted)
            mse_list.append(error)
            params.append((i,j))
    ind=mse_list.index(min(mse_list))    
    return params[ind]


##########################################estimer parametres holt amorti ##########################################
def estimate_holt_amorti(data):
    value_poss=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    mse_list=[]
    params=[]
    for i in value_poss:
        for j in value_poss:
            fit = Holt(data, damped=True).fit(smoothing_level=i, smoothing_slope=j)
            predicted=fit.fittedvalues
            error = mean_squared_error(data, predicted)
            mse_list.append(error)
            params.append((i,j))
    ind=mse_list.index(min(mse_list))    
    return params[ind]
########################################Calculer le mean square error#########################################################
def mean_sqrt(x,y):
    error = mean_squared_error(x, y)
    return error