import requests
import pandas as pd
import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from statsmodels.tsa.holtwinters import SimpleExpSmoothing, Holt
import numpy as np
from sklearn.metrics import mean_squared_error
from estimate_model import *
#%matplotlib inline
#plt.style.use('Solarize_Light2')
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import warnings
warnings.filterwarnings("ignore") # specify to ignore warning messages
#from pandas.plotting import register_matplotlib_converters
#register_matplotlib_converters()

#cov = cov = pd.read_csv('new_datav5.csv', sep=';')

def input_data(path):
    cov=pd.read_csv(path)
    return cov
###########################Split######################################

def split_data(data,k):
    data1=data['Senegal'][0:k]
    data2=data['Senegal'][k:]
    return data1, data2

###########################Train holt tendance linéaire###################################

def train_lineaire(data,k):
    data=split_data(data,k)
    data1=data[0]
    data2=data[1]
    temps=data1.index
    params_ln=estimate_ln_params(data1)
    predicted=func_ln(params_ln[0],params_ln[1],temps)
    predicted=pd.Series(predicted)
    data3=predicted.append(data2)
    params_holt=estimate_holt_lineaire(data3)
    fit = Holt(data3).fit(smoothing_level=params_holt[0], smoothing_slope=params_holt[1])
    return fit


###########################Train holt tendance amorti###################################

def train_amorti(data,k):
    data=split_data(data,k)
    data1=data[0]
    data2=data[1]
    temps=data1.index
    params_ln=estimate_ln_params(data1)
    predicted=func_ln(params_ln[0],params_ln[1],temps)
    predicted=pd.Series(predicted)
    data3=predicted.append(data2)
    params_holt=estimate_holt_amorti(data3)
    fit = Holt(data3, damped=True).fit(smoothing_level=params_holt[0], smoothing_slope=params_holt[1])
    return fit
##+#######################Prediction pour les 5 prochains jours#########################################
 
def prediction(fit):
    fcast = fit.forecast(5).rename("Trend")
    return fcast

#########################################################################################################################

def plot_data(data,predicted):
    plt.figure(figsize=(12,8),dpi=200)
    plt.plot(data, label="Cases") # la courbe des données réelles 
    plt.plot(predicted, label="Predicted")
    plt.legend()
    plt.show()
