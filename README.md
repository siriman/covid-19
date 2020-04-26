![covid-19image](https://user-images.githubusercontent.com/16143588/79042217-3713e780-7be5-11ea-85c5-ad96cc92e222.png)

# COVID-19 Spread Prediction
The main objective of this study is to predict the cumulative number of cases of the disease based on historical data. Its exploitation will be purely for statistical results intended for governments. The data is reliable and in no case will objectivity be shaken in this prediction and can serve as a very good basis for decision-makers.
We will use time series with Holt's reading method which we modify by adding a logarithm function as input for good modeling of the starting values.

## Data Format
We have chosen to use the data format below. In this format, we have the cumulative number of confirmed cases for each country on different dates

![data format](https://user-images.githubusercontent.com/16143588/79075306-8a6b6000-7ce1-11ea-9136-2db291e918b9.PNG)

![math_form1](https://user-images.githubusercontent.com/16143588/79889978-50d7da80-83ee-11ea-8b40-87c18a3a4993.PNG)
## 2 Proposed Model
This section presents the proposed omskHolt method. This is a chronological
method for predicting confirmed cases of COVID-19, as shown in Figure 1
![1](https://user-images.githubusercontent.com/16143588/79891579-b5943480-83f0-11ea-8dd1-57a60177fb3d.PNG)

![2](https://user-images.githubusercontent.com/16143588/79892042-669acf00-83f1-11ea-992c-7b7f06494ab4.PNG)

![3](https://user-images.githubusercontent.com/16143588/79892055-6bf81980-83f1-11ea-8614-80b380d537df.PNG)

## Step 0: Clone the projet
git clone https://github.com/siriman/covid-19-senegal.git
 
## Step 1: Install requirements
pip install -r requirements.txt
Modify **path** in main.py
download data with the **download_data** function
## Step 2:

Run **python main.py**
