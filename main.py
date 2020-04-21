from covid19_spread_prediction_omskmodel import *
from estimate_model import *

def main():
    path="./new_datav2.csv"
    k=18
    data=input_data(path)
    country_name=input("Enter the name of Country ")
    fit1, data1=train_amortized(data,country_name)
    fit2, data2=train_lineaire(data,country_name)
    predicted1=fit1.fittedvalues
    predicted2=fit2.fittedvalues
    #print(data["date"].iloc[-1])
    if mean_sqrt(data1[country_name],predicted1)<mean_sqrt(data2[country_name],predicted2):
        print(prediction(fit1,data))
        plot_data(data1[country_name],fit1.fittedvalues,data1['date'])
    else:
        print(prediction(fit2,data))
        plot_data(data2[country_name],fit2.fittedvalues, data2['date'])

if __name__ == '__main__':
    main()
