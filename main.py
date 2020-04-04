from model_covid19 import *
from estimate_model import *

def main():
    path="C:\\Users\\Lenovo\\Desktop\\covid-19-senegal\\data_v5.csv"
    k=18
    data=input_data(path)
    fit1=train_amorti(data,k)
    fit2=train_lineaire(data,k)
    predicted1=fit1.fittedvalues
    predicted2=fit2.fittedvalues
    if mean_sqrt(data['Senegal'],predicted1)<mean_sqrt(data['Senegal'],predicted2):
        print(prediction(fit1))
        plot_data(data['Senegal'],fit1.fittedvalues)
    else:
        print(prediction(fit2))
        plot_data(data['Senegal'],fit2.fittedvalues)

if __name__ == '__main__':
    main()