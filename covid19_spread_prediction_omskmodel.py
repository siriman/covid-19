import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from statsmodels.tsa.holtwinters import SimpleExpSmoothing, Holt
import numpy as np
import datetime as dt
from sklearn.metrics import mean_squared_error
from estimate_model import *
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import warnings
warnings.filterwarnings("ignore")

def input_data(path):
    cov=pd.read_csv(path)
    return cov
###########################Split###############################################################

def split_data(data,k):
    data1=data['Senegal'][0:k]
    data2=data['Senegal'][k:]
    return data1, data2

###########################Train holt linear trend#############################################

def train_lineaire(data,country_name):
    k=18
    #country_name=input_data("Enter the name of Country ")
    #data=split_data(data,k)
    #data=input_data(path)
    #data1=data[0]
    #data2=data[1]
    y=data[country_name]
    data=data.drop(data[y==0].index)
    data= data.reset_index()
    #data=data[country_name]
    params_holt=estimate_holt_lineaire(data[country_name])
    fit = Holt(data[country_name]).fit(smoothing_level=params_holt[0], smoothing_slope=params_holt[1])
    return fit, data


###########################Train holt amortized trend###################################

def train_amortized(data,country_name):
   # k=18
    y=data[country_name]
    data=data.drop(data[y==0].index)
    data= data.reset_index()
    #data=data[country_name]
    #temps=data1.index
    params_holt=estimate_holt_amorti(data[country_name])
    fit = Holt(data[country_name], damped=True).fit(smoothing_level=params_holt[0], smoothing_slope=params_holt[1])
    return fit, data
##+#######################Prediction pour les 5 prochains jours#########################################
 
def prediction(fit,df):
    fcast = fit.forecast(5).rename("Trend")
    a=pd.to_datetime(df["date"].iloc[-1])
    ind=pd.date_range(start=a,periods=6)
    fcast.index=ind[1:]
    return fcast

#########################################################################################################################

def plot_data(data,predicted, dates):
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set(xlabel="Date", ylabel="Number of confirmed cases in Senegal", title="COVID-19 spread in Senegal")
    x = [dt.datetime.strptime(d,'%d/%m/%Y').date() for d in dates]
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
    plt.plot(x,data, label="Reported total cases")
    plt.plot(x,predicted, label="OMSK Predicted total cases")
    plt.gcf().autofmt_xdate()
    plt.legend()
    plt.show()